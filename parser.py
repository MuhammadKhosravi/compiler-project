

import json
import pandas as pd


def convert_json_to_pd_table():
    with open("parser/table.json") as file:
        file_data = json.load(file)
        parse_table_json = file_data['parse_table']
        data_frame = pd.DataFrame(parse_table_json).transpose()
        data_frame = data_frame.where(pd.notnull(data_frame), None)
        return data_frame


class Parser:
    def __init__(self):
        self.parse_table = convert_json_to_pd_table()