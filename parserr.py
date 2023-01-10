import json

import pandas as pd

from ParserFiles.stack import Stack
from Language.Node import  Node
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

    def parse(self):
        scanner = self.scanner
        stack = self.stack
        parse_table = self.parse_table

        self.stack.push('0')
        counter = 0
        current_token, token_type = None, None
        while True:
            if self.need_new_token:
                current_token, token_type = scanner.get_next_token()
            current_entry = current_token if current_token in self.column_headers else token_type
            if stack.get_top().startswith('goto_'):
                current_action = stack.pop()
            else:
                current_action = parse_table[current_entry][stack.get_top()]

            print(current_action, current_token, current_entry)
            self.do_action(current_action, current_entry, current_token)
            print(stack)
            counter += 1

    def accept(self, _, __, ___):
        print('We are done!')
        Node.traverse()
        exit(0)

    def do_action(self, action_with_number, current_token, name):
        if action_with_number == 'accept':
            action = action_with_number
            number = None
        else:
            action, number = action_with_number.split('_')
        action_function = self.action_function_dict[action]
        action_function(number, current_token, name)

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
        if(pointed_grammar[2] == 'epsilon'):
            eps = Node('epsilon', False)
            children = [0, eps]
            print(pointed_grammar[0])
        else:
            children = self.stack.pop(number_of_pops=3 * len_of_rhs)
        print('########################', children, '############################')
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

