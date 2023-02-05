import json

from Node import Node
from Parser.stack import Stack
from code_gen import IntermediateCodeGenerator

all_table_info = None


def convert_json_to_object():
    global all_table_info
    string_json = ""
    with open('grammar/table.json') as file:
        string_json = file.read()
    all_table_info = json.loads(string_json)


class Parser:
    def __init__(self, scanner):
        convert_json_to_object()
        test = list(all_table_info['terminals'])
        test.extend(all_table_info['non_terminals'])
        test.remove('$accept')
        set_test = set(test)
        self.parse_table2 = all_table_info["parse_table"]
        self.column_headers = set_test
        self.terminals = all_table_info['terminals']
        self.non_terminals = all_table_info['non_terminals']
        self.firsts = all_table_info['first']
        self.follows = all_table_info['follow']
        self.grammar = all_table_info['grammar']
        self.scanner = scanner
        self.stack = Stack()
        self.action_function_dict = {'shift': self.shift, 'reduce': self.reduce, 'goto': self.goto,
                                     'accept': self.accept}
        self.need_new_token = True
        self.is_accepted = False
        self.current_token, self.token_type = None, None
        self.errors = []
        self.code_gen = IntermediateCodeGenerator(scanner.symbol_table)

    def parse(self):
        scanner = self.scanner
        stack = self.stack
        self.stack.push('0')
        counter = 0
        self.current_token, self.token_type = None, None
        while not self.is_accepted:
            if self.need_new_token:
                self.current_token, self.token_type = scanner.get_next_token()
            current_entry = self.current_token if self.current_token in self.column_headers else self.token_type
            if stack.get_top().startswith('goto_'):
                current_action = stack.pop()
            else:
                try:
                    current_action = self.parse_table2[str(stack.get_top())][current_entry]
                except:
                    current_action = None

            self.do_action(current_action, current_entry, self.current_token)

            counter += 1

        self.write_intermediate_code_to_file(self.code_gen.intermediate_code)
        # print(self.code_gen.semantic_stack)
        # print(self.code_gen.symbol_table)
        # print(self.code_gen.temp_values)

    def get_goto_non_terminal(self, row):
        non_terminal_list = []
        for state in row.keys():
            if row[state] is not None and row[state].startswith('goto'):
                non_terminal_list.append((state, row[state]))
        non_terminal_list.sort(key=lambda x: x[0])
        return non_terminal_list

    def get_follows_of_non_terminals(self, non_terminals):
        follow_list = []
        for non_terminal in non_terminals:
            follow_list += self.follows[non_terminal[0]]
        follow_list = list(set(follow_list))
        return follow_list

    def write_errors_to_file(self):
        str_errors = ''
        for error in self.errors:
            str_errors += error + '\n'
        if len(self.errors) == 0:
            str_errors = "There is no syntax error."
        with open('syntax_errors.txt', 'w') as file:
            file.write(str_errors)

    def handle_errors(self):
        current_line = self.scanner.current_line_index[0] + 1
        self.errors.append(f"#{current_line} : syntax error , illegal {self.current_token}")
        has_goto = False
        while not has_goto:
            top_of_stack = self.stack.get_top()
            row = self.parse_table2[top_of_stack]

            row_values = row.values()
            if 'goto' in str(row_values):
                has_goto = True
                goto_non_terminals = self.get_goto_non_terminal(row)
                follows = self.get_follows_of_non_terminals(goto_non_terminals)
                goto = None
                while goto is None:
                    self.current_token, self.token_type = self.scanner.get_next_token()
                    current_line = self.scanner.current_line_index[0] + 1
                    if self.current_token == '$':
                        self.errors.append(f'#{current_line + 1} : syntax error , Unexpected EOF')
                        self.write_errors_to_file()
                        Node.write_to_file(content='')
                        exit(0)
                    tmp_token_type = self.token_type
                    if self.current_token in self.scanner.language.KEYWORDS:
                        self.token_type = 'KEYWORD'
                    if self.current_token in follows or self.token_type in follows:
                        for non_terminal in goto_non_terminals:
                            if self.current_token in self.follows[non_terminal[0]] or self.token_type in self.follows[
                                non_terminal[0]]:
                                goto = non_terminal[1]
                                break

                    else:
                        self.token_type = tmp_token_type
                        self.errors.append(
                            f"#{current_line} : syntax error , discarded {self.current_token} from input")
                self.stack.push(non_terminal[0])
                goto = self.parse_table2[top_of_stack][non_terminal[0]]
                self.errors.append(f"#{current_line} : syntax error , missing {non_terminal[0]}")
                self.stack.push(Node(non_terminal[0], False))
                self.goto(goto.split('_')[1], '', '')
                self.need_new_token = False
            else:
                popped_stuff = self.stack.pop(number_of_pops=3)
                self.errors.append(f"syntax error , discarded {popped_stuff[1].string} from stack")

    def accept(self, _, __, ___):
        Node.traverse()
        self.is_accepted = True
        self.write_errors_to_file()
        self.write_semantic_errors_to_file()

    def do_action(self, action_with_number, current_token, name):
        try:
            if action_with_number == 'accept':
                action = action_with_number
                number = None
            else:
                action, number = action_with_number.split('_')
            action_function = self.action_function_dict[action]
            action_function(number, current_token, name)
        except:
            # print(self.stack)
            self.handle_errors()
            exit(10)

    def shift(self, number, current_token, name):
        self.stack.push(current_token)
        node = Node(current_token + '#' + name, True)
        self.stack.push(node)
        self.stack.push(number)
        self.need_new_token = True

    def reduce(self, number, token_type, token):
        pointed_grammar = self.grammar[number]
        # length of right-hand-side
        len_of_rhs = len(pointed_grammar[2:]) if pointed_grammar[2] != 'epsilon' else 0
        if pointed_grammar[2] == 'epsilon':
            eps = Node('epsilon', False)
            children = [0, eps]
        else:
            children = self.stack.pop(number_of_pops=3 * len_of_rhs)
        number_before_push = self.stack.get_top()
        parent = Node(pointed_grammar[0], False)
        new_children = list()
        for i in range(1, len(children), 3):
            children[i].add_parent(parent)
            new_children.append(children[i])
        parent.add_children(new_children)
        self.stack.push(pointed_grammar[0])
        current_entry = self.parse_table2[str(number_before_push)][str(self.stack.get_top())]
        self.stack.push(parent)
        self.stack.push(current_entry)
        self.need_new_token = False
        self.code_gen.code_gen(number, token)

    def goto(self, number, _, __):
        self.stack.push(number)

    def write_intermediate_code_to_file(self, code):
        with open('./output.txt', 'w') as file:
            file.write(str(code))

    def write_semantic_errors_to_file(self):
        with open('./semantic_errors.txt', 'w') as file:
            file.write('The input program is semantically correct.')
