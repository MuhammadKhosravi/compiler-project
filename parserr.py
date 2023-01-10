import json

from ordered_set import OrderedSet
import pandas as pd

from ParserFiles.stack import Stack

all_table_info = None


def convert_json_to_object():
    global all_table_info
    with open("ParserFiles/table.json") as file:
        all_table_info = json.load(file)


def get_pd_table():
    global all_table_info
    parse_table_object = all_table_info['parse_table']
    data_frame = pd.DataFrame(parse_table_object).transpose()
    data_frame = data_frame.where(pd.notnull(data_frame), None)
    return data_frame


class Parser:
    def __init__(self, scanner):
        convert_json_to_object()
        self.parse_table = get_pd_table()
        self.column_headers = set(self.parse_table.columns)
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

    def parse(self):
        scanner = self.scanner
        stack = self.stack
        parse_table = self.parse_table

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
                current_action = parse_table[current_entry][stack.get_top()]

            self.do_action(current_action, current_entry, self.current_token)

            counter += 1

    def get_goto_non_terminal(self, row):
        non_terminal_list = []
        for state in row.index.tolist():
            if row[state] is not None and row[state].startswith('goto'):
                non_terminal_list.append((state, row[state]))
        non_terminal_list.sort(key=lambda x: x[0])
        return non_terminal_list

    def get_follows_of_non_terminals(self, non_terminals):
        follow_list = []
        for non_terminal in non_terminals:
            follow_list += self.follows[non_terminal[0]]
        follow_list = list(OrderedSet(follow_list))
        return follow_list

    def write_errors_to_file(self):
        str_errors = ''
        for error in self.errors:
            str_errors += error + '\n'
        with open('syntax_errors.txt', 'w') as file:
            file.write(str_errors)

    def handle_errors(self):
        current_line = self.scanner.current_line_index[0] + 1
        self.errors.append(f"#{current_line} : syntax error , illegal {self.current_token}")
        has_goto = False
        while not has_goto:
            top_of_stack = self.stack.get_top()
            row = self.parse_table.iloc[int(top_of_stack)]
            row_values = row.values
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
                        self.errors.append(f"#{current_line} : syntax error , discarded {self.current_token} from input")
                self.stack.push(non_terminal[0])
                goto = self.parse_table[non_terminal[0]][top_of_stack]
                self.errors.append(f"#{current_line} : syntax error , missing {non_terminal[0]}")
                self.stack.push(Node(non_terminal[0], False))
                self.goto(goto.split('_')[1], '', '')
                self.need_new_token = False
            else:
                popped_stuff = self.stack.pop(number_of_pops=3)
                self.errors.append(f"syntax error , discarded {popped_stuff[1].name} from stack")

    def accept(self, _, __, ___):
        print('We are done!')
        Node.traverse()
        self.is_accepted = True
        self.write_errors_to_file()

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
            self.handle_errors()

    def shift(self, number, current_token, name):
        self.stack.push(current_token)
        node = Node(current_token + '#' + name, True)
        self.stack.push(node)
        self.stack.push(number)
        self.need_new_token = True

    def reduce(self, number, _, __):
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
        current_entry = self.parse_table[self.stack.get_top()][number_before_push]
        self.stack.push(parent)
        self.stack.push(current_entry)
        self.need_new_token = False

    def goto(self, number, _, __):
        self.stack.push(number)


class Node:
    leaves = list()
    symbols = ['(', ')', '/', '*', '-', '+', '==', '<', '[', ']', ';', ':', '{', '}', '=']

    def __init__(self, name, is_leaf):
        self.name = name
        self.parent = None
        self.children = list()
        if is_leaf:
            Node.leaves.append(self)
            if '#' in name:
                joint = name.split('#')
                self.name = '(' + joint[0] + ', ' + joint[1] + ')'
                if joint[0] == joint[1]:
                    if joint[0] in Node.symbols:
                        self.name = '(SYMBOL, ' + joint[0] + ')'
                    else:
                        self.name = 'KEYWORD, ' + joint[0] + ')'

    def add_parent(self, parent):
        self.parent = parent

    def add_children(self, children):
        self.children.extend(children)

    def __str__(self):
        return self.name

    def traverse():
        max_depth = 0
        for node in Node.leaves:
            depth = 0
            node_temp = node
            while type(node_temp) == Node:
                if type(node_temp.parent) == Node:
                    root = node_temp
                node_temp = node_temp.parent
                depth += 1
            if depth > max_depth:
                max_depth = depth
        root_main = Node('program', False)
        root_main.add_children([root])
        root.add_parent(root_main)
        queue = [[root_main]]
        for i in range(max_depth):
            children = list()
            for nodes in queue:
                for node in nodes:
                    children.append(node.children.__reversed__())
            queue = children