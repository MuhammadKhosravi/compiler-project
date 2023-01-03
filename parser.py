import json
import pandas as pd

from Parser.stack import Stack

all_table_info = None


def convert_json_to_object():
    global all_table_info
    with open("Parser/table.json") as file:
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
        self.terminals = all_table_info['terminals']
        self.non_terminals = all_table_info['non_terminals']
        self.firsts = all_table_info['first']
        self.follows = all_table_info['follow']
        self.grammar = all_table_info['grammar']
        self.scanner = scanner
        self.stack = Stack()
        self.action_function_dict = {'shift': self.shift, 'reduce': self.reduce, 'goto': self.goto}

    def parse(self):
        scanner = self.scanner
        self.stack.push('shift_0')
        while True:
            current_token = scanner.get_next_token()
            print(current_token)
            if current_token == '$':
                break
        # print(scanner.symbol_table)
        # print(scanner.errors)

    def do_action(self, action_number):
        action, number = action_number.split('_')
        action_function = self.action_function_dict[action]
        action_function(action_number)

    def shift(self):
        pass

    def reduce(self):
        pass

    def goto(self):
        pass
