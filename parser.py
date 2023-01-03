import json
import pandas as pd

all_table_info = None


def convert_json_to_object():
    global all_table_info
    with open("parser/table.json") as file:
        all_table_info = json.load(file)


def get_pd_table():
    global all_table_info
    parse_table_object = all_table_info['parse_table']
    data_frame = pd.DataFrame(parse_table_object).transpose()
    data_frame = data_frame.where(pd.notnull(data_frame), None)
    return data_frame


class Parser:
    def __init__(self):
        convert_json_to_object()
        self.parse_table = get_pd_table()
        self.terminals = all_table_info['terminals']
        self.non_terminals = all_table_info['non_terminals']
        self.firsts = all_table_info['first']
        self.follows = all_table_info['follow']
