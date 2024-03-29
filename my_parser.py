import json

from stack import Stack
from Node import Node

all_table_info = None


def convert_json_to_object():
    global all_table_info
    string_json = '''{
    "terminals": [
        "$",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        "/",
        ":",
        ";",
        "<",
        "=",
        "[",
        "]",
        "{",
        "}",
        "NUM",
        "ID",
        "int",
        "void",
        "break",
        "if",
        "endif",
        "else",
        "while",
        "return",
        "switch",
        "case",
        "default",
        "=="
    ],
    "non_terminals": [
        "$accept",
        "program",
        "declaration_list",
        "declaration",
        "var_declaration",
        "type_specifier",
        "fun_declaration",
        "params",
        "param_list",
        "param",
        "compound_stmt",
        "local_declarations",
        "statement_list",
        "statement",
        "expression_stmt",
        "selection_stmt",
        "iteration_stmt",
        "return_stmt",
        "switch_stmt",
        "case_stmts",
        "case_stmt",
        "default_stmt",
        "expression",
        "var",
        "simple_expression",
        "relop",
        "additive_expression",
        "addop",
        "term",
        "mulop",
        "factor",
        "call",
        "args",
        "arg_list"
    ],
    "first": {
        "$accept": [
            "void",
            "int"
        ],
        "program": [
            "void",
            "int"
        ],
        "declaration_list": [
            "void",
            "int"
        ],
        "declaration": [
            "void",
            "int"
        ],
        "var_declaration": [
            "void",
            "int"
        ],
        "type_specifier": [
            "void",
            "int"
        ],
        "fun_declaration": [
            "void",
            "int"
        ],
        "params": [
            "void",
            "int"
        ],
        "param_list": [
            "void",
            "int"
        ],
        "param": [
            "void",
            "int"
        ],
        "compound_stmt": [
            "{"
        ],
        "local_declarations": [
            "void",
            "int"
        ],
        "statement_list": [
            ";",
            "if",
            "switch",
            "(",
            "break",
            "ID",
            "while",
            "return",
            "{",
            "NUM"
        ],
        "statement": [
            ";",
            "if",
            "switch",
            "return",
            "{",
            "break",
            "(",
            "ID",
            "NUM",
            "while"
        ],
        "expression_stmt": [
            "(",
            "break",
            ";",
            "ID",
            "NUM"
        ],
        "selection_stmt": [
            "if"
        ],
        "iteration_stmt": [
            "while"
        ],
        "return_stmt": [
            "return"
        ],
        "switch_stmt": [
            "switch"
        ],
        "case_stmts": [
            "case"
        ],
        "case_stmt": [
            "case"
        ],
        "default_stmt": [
            "default"
        ],
        "expression": [
            "(",
            "ID",
            "NUM"
        ],
        "var": [
            "ID"
        ],
        "simple_expression": [
            "(",
            "ID",
            "NUM"
        ],
        "relop": [
            "==",
            "<"
        ],
        "additive_expression": [
            "(",
            "ID",
            "NUM"
        ],
        "addop": [
            "-",
            "+"
        ],
        "term": [
            "(",
            "ID",
            "NUM"
        ],
        "mulop": [
            "*",
            "/"
        ],
        "factor": [
            "ID",
            "NUM",
            "("
        ],
        "call": [
            "ID"
        ],
        "args": [
            "(",
            "ID",
            "NUM"
        ],
        "arg_list": [
            "(",
            "ID",
            "NUM"
        ],
        "$": [
            "$"
        ],
        "(": [
            "("
        ],
        ")": [
            ")"
        ],
        "*": [
            "*"
        ],
        "+": [
            "+"
        ],
        ",": [
            ","
        ],
        "-": [
            "-"
        ],
        "/": [
            "/"
        ],
        ":": [
            ":"
        ],
        ";": [
            ";"
        ],
        "<": [
            "<"
        ],
        "=": [
            "="
        ],
        "[": [
            "["
        ],
        "]": [
            "]"
        ],
        "{": [
            "{"
        ],
        "}": [
            "}"
        ],
        "NUM": [
            "NUM"
        ],
        "ID": [
            "ID"
        ],
        "int": [
            "int"
        ],
        "void": [
            "void"
        ],
        "break": [
            "break"
        ],
        "if": [
            "if"
        ],
        "endif": [
            "endif"
        ],
        "else": [
            "else"
        ],
        "while": [
            "while"
        ],
        "return": [
            "return"
        ],
        "switch": [
            "switch"
        ],
        "case": [
            "case"
        ],
        "default": [
            "default"
        ],
        "==": [
            "=="
        ]
    },
    "follow": {
        "$accept": [],
        "program": [
            "$"
        ],
        "declaration_list": [
            "int",
            "void",
            "$"
        ],
        "declaration": [
            "int",
            "void",
            "$"
        ],
        "var_declaration": [
            "void",
            ";",
            "if",
            "switch",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "int",
            "return",
            "{",
            "NUM",
            "$"
        ],
        "type_specifier": [
            "ID"
        ],
        "fun_declaration": [
            "int",
            "void",
            "$"
        ],
        "params": [
            ")"
        ],
        "param_list": [
            ",",
            ")"
        ],
        "param": [
            ",",
            ")"
        ],
        "compound_stmt": [
            "void",
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "int",
            "endif",
            "else",
            "return",
            "{",
            "NUM",
            "$"
        ],
        "local_declarations": [
            "void",
            ";",
            "if",
            "switch",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "int",
            "return",
            "{",
            "NUM"
        ],
        "statement_list": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "return",
            "{",
            "NUM"
        ],
        "statement": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "expression_stmt": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "selection_stmt": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "iteration_stmt": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "return_stmt": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "switch_stmt": [
            ";",
            "if",
            "switch",
            "case",
            "}",
            "(",
            "break",
            "ID",
            "while",
            "default",
            "endif",
            "else",
            "return",
            "{",
            "NUM"
        ],
        "case_stmts": [
            "}",
            "case",
            "default"
        ],
        "case_stmt": [
            "}",
            "case",
            "default"
        ],
        "default_stmt": [
            "}"
        ],
        "expression": [
            ";",
            "]",
            ",",
            ")"
        ],
        "var": [
            "*",
            ";",
            "-",
            "+",
            "<",
            ",",
            "==",
            "/",
            "=",
            "]",
            ")"
        ],
        "simple_expression": [
            ";",
            "]",
            ",",
            ")"
        ],
        "relop": [
            "(",
            "ID",
            "NUM"
        ],
        "additive_expression": [
            ";",
            "==",
            "-",
            ",",
            "+",
            "<",
            "]",
            ")"
        ],
        "addop": [
            "(",
            "ID",
            "NUM"
        ],
        "term": [
            "]",
            ";",
            "*",
            "==",
            "-",
            "+",
            "/",
            "<",
            ",",
            ")"
        ],
        "mulop": [
            "(",
            "ID",
            "NUM"
        ],
        "factor": [
            "*",
            ";",
            "-",
            "+",
            "<",
            ",",
            "==",
            "/",
            "]",
            ")"
        ],
        "call": [
            "*",
            ";",
            "-",
            "+",
            "<",
            ",",
            "==",
            "/",
            "]",
            ")"
        ],
        "args": [
            ")"
        ],
        "arg_list": [
            ",",
            ")"
        ]
    },
    "grammar": {
        "0": [
            "$accept",
            "->",
            "program",
            "$"
        ],
        "1": [
            "program",
            "->",
            "declaration_list"
        ],
        "2": [
            "declaration_list",
            "->",
            "declaration_list",
            "declaration"
        ],
        "3": [
            "declaration_list",
            "->",
            "declaration"
        ],
        "4": [
            "declaration",
            "->",
            "var_declaration"
        ],
        "5": [
            "declaration",
            "->",
            "fun_declaration"
        ],
        "6": [
            "var_declaration",
            "->",
            "type_specifier",
            "ID",
            ";"
        ],
        "7": [
            "var_declaration",
            "->",
            "type_specifier",
            "ID",
            "[",
            "NUM",
            "]",
            ";"
        ],
        "8": [
            "type_specifier",
            "->",
            "int"
        ],
        "9": [
            "type_specifier",
            "->",
            "void"
        ],
        "10": [
            "fun_declaration",
            "->",
            "type_specifier",
            "ID",
            "(",
            "params",
            ")",
            "compound_stmt"
        ],
        "11": [
            "params",
            "->",
            "param_list"
        ],
        "12": [
            "params",
            "->",
            "void"
        ],
        "13": [
            "param_list",
            "->",
            "param_list",
            ",",
            "param"
        ],
        "14": [
            "param_list",
            "->",
            "param"
        ],
        "15": [
            "param",
            "->",
            "type_specifier",
            "ID"
        ],
        "16": [
            "param",
            "->",
            "type_specifier",
            "ID",
            "[",
            "]"
        ],
        "17": [
            "compound_stmt",
            "->",
            "{",
            "local_declarations",
            "statement_list",
            "}"
        ],
        "18": [
            "local_declarations",
            "->",
            "local_declarations",
            "var_declaration"
        ],
        "19": [
            "local_declarations",
            "->",
            "epsilon"
        ],
        "20": [
            "statement_list",
            "->",
            "statement_list",
            "statement"
        ],
        "21": [
            "statement_list",
            "->",
            "epsilon"
        ],
        "22": [
            "statement",
            "->",
            "expression_stmt"
        ],
        "23": [
            "statement",
            "->",
            "compound_stmt"
        ],
        "24": [
            "statement",
            "->",
            "selection_stmt"
        ],
        "25": [
            "statement",
            "->",
            "iteration_stmt"
        ],
        "26": [
            "statement",
            "->",
            "return_stmt"
        ],
        "27": [
            "statement",
            "->",
            "switch_stmt"
        ],
        "28": [
            "expression_stmt",
            "->",
            "expression",
            ";"
        ],
        "29": [
            "expression_stmt",
            "->",
            "break",
            ";"
        ],
        "30": [
            "expression_stmt",
            "->",
            ";"
        ],
        "31": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "statement",
            "endif"
        ],
        "32": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "statement",
            "else",
            "statement",
            "endif"
        ],
        "33": [
            "iteration_stmt",
            "->",
            "while",
            "(",
            "expression",
            ")",
            "statement"
        ],
        "34": [
            "return_stmt",
            "->",
            "return",
            ";"
        ],
        "35": [
            "return_stmt",
            "->",
            "return",
            "expression",
            ";"
        ],
        "36": [
            "switch_stmt",
            "->",
            "switch",
            "(",
            "expression",
            ")",
            "{",
            "case_stmts",
            "default_stmt",
            "}"
        ],
        "37": [
            "case_stmts",
            "->",
            "case_stmts",
            "case_stmt"
        ],
        "38": [
            "case_stmts",
            "->",
            "epsilon"
        ],
        "39": [
            "case_stmt",
            "->",
            "case",
            "NUM",
            ":",
            "statement_list"
        ],
        "40": [
            "default_stmt",
            "->",
            "default",
            ":",
            "statement_list"
        ],
        "41": [
            "default_stmt",
            "->",
            "epsilon"
        ],
        "42": [
            "expression",
            "->",
            "var",
            "=",
            "expression"
        ],
        "43": [
            "expression",
            "->",
            "simple_expression"
        ],
        "44": [
            "var",
            "->",
            "ID"
        ],
        "45": [
            "var",
            "->",
            "ID",
            "[",
            "expression",
            "]"
        ],
        "46": [
            "simple_expression",
            "->",
            "additive_expression",
            "relop",
            "additive_expression"
        ],
        "47": [
            "simple_expression",
            "->",
            "additive_expression"
        ],
        "48": [
            "relop",
            "->",
            "<"
        ],
        "49": [
            "relop",
            "->",
            "=="
        ],
        "50": [
            "additive_expression",
            "->",
            "additive_expression",
            "addop",
            "term"
        ],
        "51": [
            "additive_expression",
            "->",
            "term"
        ],
        "52": [
            "addop",
            "->",
            "+"
        ],
        "53": [
            "addop",
            "->",
            "-"
        ],
        "54": [
            "term",
            "->",
            "term",
            "mulop",
            "factor"
        ],
        "55": [
            "term",
            "->",
            "factor"
        ],
        "56": [
            "mulop",
            "->",
            "*"
        ],
        "57": [
            "mulop",
            "->",
            "/"
        ],
        "58": [
            "factor",
            "->",
            "(",
            "expression",
            ")"
        ],
        "59": [
            "factor",
            "->",
            "var"
        ],
        "60": [
            "factor",
            "->",
            "call"
        ],
        "61": [
            "factor",
            "->",
            "NUM"
        ],
        "62": [
            "call",
            "->",
            "ID",
            "(",
            "args",
            ")"
        ],
        "63": [
            "args",
            "->",
            "arg_list"
        ],
        "64": [
            "args",
            "->",
            "epsilon"
        ],
        "65": [
            "arg_list",
            "->",
            "arg_list",
            ",",
            "expression"
        ],
        "66": [
            "arg_list",
            "->",
            "expression"
        ]
    },
    "parse_table": {
        "0": {
            "int": "shift_1",
            "void": "shift_2",
            "program": "goto_3",
            "declaration_list": "goto_4",
            "declaration": "goto_5",
            "var_declaration": "goto_6",
            "type_specifier": "goto_7",
            "fun_declaration": "goto_8"
        },
        "1": {
            "ID": "reduce_8"
        },
        "2": {
            "ID": "reduce_9"
        },
        "3": {
            "$": "shift_9"
        },
        "4": {
            "int": "shift_1",
            "void": "shift_2",
            "declaration": "goto_10",
            "var_declaration": "goto_6",
            "type_specifier": "goto_7",
            "fun_declaration": "goto_8",
            "$": "reduce_1"
        },
        "5": {
            "int": "reduce_3",
            "void": "reduce_3",
            "$": "reduce_3"
        },
        "6": {
            "int": "reduce_4",
            "void": "reduce_4",
            "$": "reduce_4"
        },
        "7": {
            "ID": "shift_11"
        },
        "8": {
            "int": "reduce_5",
            "void": "reduce_5",
            "$": "reduce_5"
        },
        "9": {
            "$": "accept"
        },
        "10": {
            "int": "reduce_2",
            "void": "reduce_2",
            "$": "reduce_2"
        },
        "11": {
            ";": "shift_12",
            "[": "shift_13",
            "(": "shift_14"
        },
        "12": {
            "void": "reduce_6",
            ";": "reduce_6",
            "if": "reduce_6",
            "switch": "reduce_6",
            "}": "reduce_6",
            "(": "reduce_6",
            "break": "reduce_6",
            "ID": "reduce_6",
            "while": "reduce_6",
            "int": "reduce_6",
            "return": "reduce_6",
            "{": "reduce_6",
            "NUM": "reduce_6",
            "$": "reduce_6"
        },
        "13": {
            "NUM": "shift_15"
        },
        "14": {
            "int": "shift_1",
            "void": "shift_16",
            "type_specifier": "goto_17",
            "params": "goto_18",
            "param_list": "goto_19",
            "param": "goto_20"
        },
        "15": {
            "]": "shift_21"
        },
        "16": {
            ")": "reduce_12",
            "ID": "reduce_9"
        },
        "17": {
            "ID": "shift_22"
        },
        "18": {
            ")": "shift_23"
        },
        "19": {
            ",": "shift_24",
            ")": "reduce_11"
        },
        "20": {
            ",": "reduce_14",
            ")": "reduce_14"
        },
        "21": {
            ";": "shift_25"
        },
        "22": {
            "[": "shift_26",
            ",": "reduce_15",
            ")": "reduce_15"
        },
        "23": {
            "{": "shift_27",
            "compound_stmt": "goto_28"
        },
        "24": {
            "int": "shift_1",
            "void": "shift_2",
            "type_specifier": "goto_17",
            "param": "goto_29"
        },
        "25": {
            "void": "reduce_7",
            ";": "reduce_7",
            "if": "reduce_7",
            "switch": "reduce_7",
            "}": "reduce_7",
            "(": "reduce_7",
            "break": "reduce_7",
            "ID": "reduce_7",
            "while": "reduce_7",
            "int": "reduce_7",
            "return": "reduce_7",
            "{": "reduce_7",
            "NUM": "reduce_7",
            "$": "reduce_7"
        },
        "26": {
            "]": "shift_30"
        },
        "27": {
            "local_declarations": "goto_31",
            "void": "reduce_19",
            ";": "reduce_19",
            "if": "reduce_19",
            "switch": "reduce_19",
            "}": "reduce_19",
            "(": "reduce_19",
            "break": "reduce_19",
            "ID": "reduce_19",
            "while": "reduce_19",
            "int": "reduce_19",
            "return": "reduce_19",
            "{": "reduce_19",
            "NUM": "reduce_19"
        },
        "28": {
            "int": "reduce_10",
            "void": "reduce_10",
            "$": "reduce_10"
        },
        "29": {
            ",": "reduce_13",
            ")": "reduce_13"
        },
        "30": {
            ",": "reduce_16",
            ")": "reduce_16"
        },
        "31": {
            "int": "shift_1",
            "void": "shift_2",
            "var_declaration": "goto_32",
            "type_specifier": "goto_33",
            "statement_list": "goto_34",
            ";": "reduce_21",
            "if": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "}": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "ID": "reduce_21",
            "while": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21"
        },
        "32": {
            "void": "reduce_18",
            ";": "reduce_18",
            "if": "reduce_18",
            "switch": "reduce_18",
            "}": "reduce_18",
            "(": "reduce_18",
            "break": "reduce_18",
            "ID": "reduce_18",
            "while": "reduce_18",
            "int": "reduce_18",
            "return": "reduce_18",
            "{": "reduce_18",
            "NUM": "reduce_18"
        },
        "33": {
            "ID": "shift_35"
        },
        "34": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "}": "shift_40",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_47",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "35": {
            ";": "shift_12",
            "[": "shift_13"
        },
        "36": {
            "*": "reduce_61",
            ";": "reduce_61",
            "-": "reduce_61",
            "+": "reduce_61",
            "<": "reduce_61",
            ",": "reduce_61",
            "==": "reduce_61",
            "/": "reduce_61",
            "]": "reduce_61",
            ")": "reduce_61"
        },
        "37": {
            "[": "shift_60",
            "(": "shift_61",
            "*": "reduce_44",
            ";": "reduce_44",
            "-": "reduce_44",
            "+": "reduce_44",
            "<": "reduce_44",
            ",": "reduce_44",
            "==": "reduce_44",
            "/": "reduce_44",
            "=": "reduce_44",
            "]": "reduce_44",
            ")": "reduce_44"
        },
        "38": {
            ";": "reduce_30",
            "if": "reduce_30",
            "switch": "reduce_30",
            "case": "reduce_30",
            "}": "reduce_30",
            "(": "reduce_30",
            "break": "reduce_30",
            "ID": "reduce_30",
            "while": "reduce_30",
            "default": "reduce_30",
            "endif": "reduce_30",
            "else": "reduce_30",
            "return": "reduce_30",
            "{": "reduce_30",
            "NUM": "reduce_30"
        },
        "39": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_62",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "40": {
            "void": "reduce_17",
            ";": "reduce_17",
            "if": "reduce_17",
            "switch": "reduce_17",
            "case": "reduce_17",
            "}": "reduce_17",
            "(": "reduce_17",
            "break": "reduce_17",
            "ID": "reduce_17",
            "while": "reduce_17",
            "default": "reduce_17",
            "int": "reduce_17",
            "endif": "reduce_17",
            "else": "reduce_17",
            "return": "reduce_17",
            "{": "reduce_17",
            "NUM": "reduce_17",
            "$": "reduce_17"
        },
        "41": {
            ";": "shift_63"
        },
        "42": {
            "(": "shift_64"
        },
        "43": {
            "(": "shift_65"
        },
        "44": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_66",
            "(": "shift_39",
            "expression": "goto_67",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "45": {
            "(": "shift_68"
        },
        "46": {
            ";": "reduce_23",
            "if": "reduce_23",
            "switch": "reduce_23",
            "case": "reduce_23",
            "}": "reduce_23",
            "(": "reduce_23",
            "break": "reduce_23",
            "ID": "reduce_23",
            "while": "reduce_23",
            "default": "reduce_23",
            "endif": "reduce_23",
            "else": "reduce_23",
            "return": "reduce_23",
            "{": "reduce_23",
            "NUM": "reduce_23"
        },
        "47": {
            ";": "reduce_20",
            "if": "reduce_20",
            "switch": "reduce_20",
            "case": "reduce_20",
            "}": "reduce_20",
            "(": "reduce_20",
            "break": "reduce_20",
            "ID": "reduce_20",
            "while": "reduce_20",
            "default": "reduce_20",
            "return": "reduce_20",
            "{": "reduce_20",
            "NUM": "reduce_20"
        },
        "48": {
            ";": "reduce_22",
            "if": "reduce_22",
            "switch": "reduce_22",
            "case": "reduce_22",
            "}": "reduce_22",
            "(": "reduce_22",
            "break": "reduce_22",
            "ID": "reduce_22",
            "while": "reduce_22",
            "default": "reduce_22",
            "endif": "reduce_22",
            "else": "reduce_22",
            "return": "reduce_22",
            "{": "reduce_22",
            "NUM": "reduce_22"
        },
        "49": {
            ";": "reduce_24",
            "if": "reduce_24",
            "switch": "reduce_24",
            "case": "reduce_24",
            "}": "reduce_24",
            "(": "reduce_24",
            "break": "reduce_24",
            "ID": "reduce_24",
            "while": "reduce_24",
            "default": "reduce_24",
            "endif": "reduce_24",
            "else": "reduce_24",
            "return": "reduce_24",
            "{": "reduce_24",
            "NUM": "reduce_24"
        },
        "50": {
            ";": "reduce_25",
            "if": "reduce_25",
            "switch": "reduce_25",
            "case": "reduce_25",
            "}": "reduce_25",
            "(": "reduce_25",
            "break": "reduce_25",
            "ID": "reduce_25",
            "while": "reduce_25",
            "default": "reduce_25",
            "endif": "reduce_25",
            "else": "reduce_25",
            "return": "reduce_25",
            "{": "reduce_25",
            "NUM": "reduce_25"
        },
        "51": {
            ";": "reduce_26",
            "if": "reduce_26",
            "switch": "reduce_26",
            "case": "reduce_26",
            "}": "reduce_26",
            "(": "reduce_26",
            "break": "reduce_26",
            "ID": "reduce_26",
            "while": "reduce_26",
            "default": "reduce_26",
            "endif": "reduce_26",
            "else": "reduce_26",
            "return": "reduce_26",
            "{": "reduce_26",
            "NUM": "reduce_26"
        },
        "52": {
            ";": "reduce_27",
            "if": "reduce_27",
            "switch": "reduce_27",
            "case": "reduce_27",
            "}": "reduce_27",
            "(": "reduce_27",
            "break": "reduce_27",
            "ID": "reduce_27",
            "while": "reduce_27",
            "default": "reduce_27",
            "endif": "reduce_27",
            "else": "reduce_27",
            "return": "reduce_27",
            "{": "reduce_27",
            "NUM": "reduce_27"
        },
        "53": {
            ";": "shift_69"
        },
        "54": {
            "=": "shift_70",
            "*": "reduce_59",
            ";": "reduce_59",
            "-": "reduce_59",
            "+": "reduce_59",
            "<": "reduce_59",
            ",": "reduce_59",
            "==": "reduce_59",
            "/": "reduce_59",
            "]": "reduce_59",
            ")": "reduce_59"
        },
        "55": {
            ";": "reduce_43",
            "]": "reduce_43",
            ",": "reduce_43",
            ")": "reduce_43"
        },
        "56": {
            "<": "shift_71",
            "==": "shift_72",
            "+": "shift_73",
            "-": "shift_74",
            "relop": "goto_75",
            "addop": "goto_76",
            ";": "reduce_47",
            "]": "reduce_47",
            ",": "reduce_47",
            ")": "reduce_47"
        },
        "57": {
            "*": "shift_77",
            "/": "shift_78",
            "mulop": "goto_79",
            ";": "reduce_51",
            "==": "reduce_51",
            "-": "reduce_51",
            ",": "reduce_51",
            "+": "reduce_51",
            "<": "reduce_51",
            "]": "reduce_51",
            ")": "reduce_51"
        },
        "58": {
            "]": "reduce_55",
            ";": "reduce_55",
            "*": "reduce_55",
            "==": "reduce_55",
            "-": "reduce_55",
            "+": "reduce_55",
            "/": "reduce_55",
            "<": "reduce_55",
            ",": "reduce_55",
            ")": "reduce_55"
        },
        "59": {
            "*": "reduce_60",
            ";": "reduce_60",
            "-": "reduce_60",
            "+": "reduce_60",
            "<": "reduce_60",
            ",": "reduce_60",
            "==": "reduce_60",
            "/": "reduce_60",
            "]": "reduce_60",
            ")": "reduce_60"
        },
        "60": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_80",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "61": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_81",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59",
            "args": "goto_82",
            "arg_list": "goto_83",
            ")": "reduce_64"
        },
        "62": {
            ")": "shift_84"
        },
        "63": {
            ";": "reduce_29",
            "if": "reduce_29",
            "switch": "reduce_29",
            "case": "reduce_29",
            "}": "reduce_29",
            "(": "reduce_29",
            "break": "reduce_29",
            "ID": "reduce_29",
            "while": "reduce_29",
            "default": "reduce_29",
            "endif": "reduce_29",
            "else": "reduce_29",
            "return": "reduce_29",
            "{": "reduce_29",
            "NUM": "reduce_29"
        },
        "64": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_85",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "65": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_86",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "66": {
            ";": "reduce_34",
            "if": "reduce_34",
            "switch": "reduce_34",
            "case": "reduce_34",
            "}": "reduce_34",
            "(": "reduce_34",
            "break": "reduce_34",
            "ID": "reduce_34",
            "while": "reduce_34",
            "default": "reduce_34",
            "endif": "reduce_34",
            "else": "reduce_34",
            "return": "reduce_34",
            "{": "reduce_34",
            "NUM": "reduce_34"
        },
        "67": {
            ";": "shift_87"
        },
        "68": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_88",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "69": {
            ";": "reduce_28",
            "if": "reduce_28",
            "switch": "reduce_28",
            "case": "reduce_28",
            "}": "reduce_28",
            "(": "reduce_28",
            "break": "reduce_28",
            "ID": "reduce_28",
            "while": "reduce_28",
            "default": "reduce_28",
            "endif": "reduce_28",
            "else": "reduce_28",
            "return": "reduce_28",
            "{": "reduce_28",
            "NUM": "reduce_28"
        },
        "70": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_89",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "71": {
            "(": "reduce_48",
            "ID": "reduce_48",
            "NUM": "reduce_48"
        },
        "72": {
            "(": "reduce_49",
            "ID": "reduce_49",
            "NUM": "reduce_49"
        },
        "73": {
            "(": "reduce_52",
            "ID": "reduce_52",
            "NUM": "reduce_52"
        },
        "74": {
            "(": "reduce_53",
            "ID": "reduce_53",
            "NUM": "reduce_53"
        },
        "75": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "var": "goto_90",
            "additive_expression": "goto_91",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "76": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "var": "goto_90",
            "term": "goto_92",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "77": {
            "(": "reduce_56",
            "ID": "reduce_56",
            "NUM": "reduce_56"
        },
        "78": {
            "(": "reduce_57",
            "ID": "reduce_57",
            "NUM": "reduce_57"
        },
        "79": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "var": "goto_90",
            "factor": "goto_93",
            "call": "goto_59"
        },
        "80": {
            "]": "shift_94"
        },
        "81": {
            ",": "reduce_66",
            ")": "reduce_66"
        },
        "82": {
            ")": "shift_95"
        },
        "83": {
            ",": "shift_96",
            ")": "reduce_63"
        },
        "84": {
            "*": "reduce_58",
            ";": "reduce_58",
            "-": "reduce_58",
            "+": "reduce_58",
            "<": "reduce_58",
            ",": "reduce_58",
            "==": "reduce_58",
            "/": "reduce_58",
            "]": "reduce_58",
            ")": "reduce_58"
        },
        "85": {
            ")": "shift_97"
        },
        "86": {
            ")": "shift_98"
        },
        "87": {
            ";": "reduce_35",
            "if": "reduce_35",
            "switch": "reduce_35",
            "case": "reduce_35",
            "}": "reduce_35",
            "(": "reduce_35",
            "break": "reduce_35",
            "ID": "reduce_35",
            "while": "reduce_35",
            "default": "reduce_35",
            "endif": "reduce_35",
            "else": "reduce_35",
            "return": "reduce_35",
            "{": "reduce_35",
            "NUM": "reduce_35"
        },
        "88": {
            ")": "shift_99"
        },
        "89": {
            ";": "reduce_42",
            "]": "reduce_42",
            ",": "reduce_42",
            ")": "reduce_42"
        },
        "90": {
            "*": "reduce_59",
            ";": "reduce_59",
            "-": "reduce_59",
            "+": "reduce_59",
            "<": "reduce_59",
            ",": "reduce_59",
            "==": "reduce_59",
            "/": "reduce_59",
            "]": "reduce_59",
            ")": "reduce_59"
        },
        "91": {
            "+": "shift_73",
            "-": "shift_74",
            "addop": "goto_76",
            ";": "reduce_46",
            "]": "reduce_46",
            ",": "reduce_46",
            ")": "reduce_46"
        },
        "92": {
            "*": "shift_77",
            "/": "shift_78",
            "mulop": "goto_79",
            ";": "reduce_50",
            "==": "reduce_50",
            "-": "reduce_50",
            ",": "reduce_50",
            "+": "reduce_50",
            "<": "reduce_50",
            "]": "reduce_50",
            ")": "reduce_50"
        },
        "93": {
            "]": "reduce_54",
            ";": "reduce_54",
            "*": "reduce_54",
            "==": "reduce_54",
            "-": "reduce_54",
            "+": "reduce_54",
            "/": "reduce_54",
            "<": "reduce_54",
            ",": "reduce_54",
            ")": "reduce_54"
        },
        "94": {
            "*": "reduce_45",
            ";": "reduce_45",
            "-": "reduce_45",
            "+": "reduce_45",
            "<": "reduce_45",
            ",": "reduce_45",
            "==": "reduce_45",
            "/": "reduce_45",
            "=": "reduce_45",
            "]": "reduce_45",
            ")": "reduce_45"
        },
        "95": {
            "*": "reduce_62",
            ";": "reduce_62",
            "-": "reduce_62",
            "+": "reduce_62",
            "<": "reduce_62",
            ",": "reduce_62",
            "==": "reduce_62",
            "/": "reduce_62",
            "]": "reduce_62",
            ")": "reduce_62"
        },
        "96": {
            "NUM": "shift_36",
            "ID": "shift_37",
            "(": "shift_39",
            "expression": "goto_100",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "97": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_101",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "98": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_102",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "99": {
            "{": "shift_103"
        },
        "100": {
            ",": "reduce_65",
            ")": "reduce_65"
        },
        "101": {
            "endif": "shift_104",
            "else": "shift_105"
        },
        "102": {
            ";": "reduce_33",
            "if": "reduce_33",
            "switch": "reduce_33",
            "case": "reduce_33",
            "}": "reduce_33",
            "(": "reduce_33",
            "break": "reduce_33",
            "ID": "reduce_33",
            "while": "reduce_33",
            "default": "reduce_33",
            "endif": "reduce_33",
            "else": "reduce_33",
            "return": "reduce_33",
            "{": "reduce_33",
            "NUM": "reduce_33"
        },
        "103": {
            "case_stmts": "goto_106",
            "}": "reduce_38",
            "case": "reduce_38",
            "default": "reduce_38"
        },
        "104": {
            ";": "reduce_31",
            "if": "reduce_31",
            "switch": "reduce_31",
            "case": "reduce_31",
            "}": "reduce_31",
            "(": "reduce_31",
            "break": "reduce_31",
            "ID": "reduce_31",
            "while": "reduce_31",
            "default": "reduce_31",
            "endif": "reduce_31",
            "else": "reduce_31",
            "return": "reduce_31",
            "{": "reduce_31",
            "NUM": "reduce_31"
        },
        "105": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_107",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59"
        },
        "106": {
            "case": "shift_108",
            "default": "shift_109",
            "case_stmt": "goto_110",
            "default_stmt": "goto_111",
            "}": "reduce_41"
        },
        "107": {
            "endif": "shift_112"
        },
        "108": {
            "NUM": "shift_113"
        },
        "109": {
            ":": "shift_114"
        },
        "110": {
            "}": "reduce_37",
            "case": "reduce_37",
            "default": "reduce_37"
        },
        "111": {
            "}": "shift_115"
        },
        "112": {
            ";": "reduce_32",
            "if": "reduce_32",
            "switch": "reduce_32",
            "case": "reduce_32",
            "}": "reduce_32",
            "(": "reduce_32",
            "break": "reduce_32",
            "ID": "reduce_32",
            "while": "reduce_32",
            "default": "reduce_32",
            "endif": "reduce_32",
            "else": "reduce_32",
            "return": "reduce_32",
            "{": "reduce_32",
            "NUM": "reduce_32"
        },
        "113": {
            ":": "shift_116"
        },
        "114": {
            "statement_list": "goto_117",
            ";": "reduce_21",
            "if": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "}": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "ID": "reduce_21",
            "while": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21"
        },
        "115": {
            ";": "reduce_36",
            "if": "reduce_36",
            "switch": "reduce_36",
            "case": "reduce_36",
            "}": "reduce_36",
            "(": "reduce_36",
            "break": "reduce_36",
            "ID": "reduce_36",
            "while": "reduce_36",
            "default": "reduce_36",
            "endif": "reduce_36",
            "else": "reduce_36",
            "return": "reduce_36",
            "{": "reduce_36",
            "NUM": "reduce_36"
        },
        "116": {
            "statement_list": "goto_118",
            ";": "reduce_21",
            "if": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "}": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "ID": "reduce_21",
            "while": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21"
        },
        "117": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_47",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59",
            "}": "reduce_40"
        },
        "118": {
            "NUM": "shift_36",
            "ID": "shift_37",
            ";": "shift_38",
            "(": "shift_39",
            "{": "shift_27",
            "break": "shift_41",
            "if": "shift_42",
            "while": "shift_43",
            "return": "shift_44",
            "switch": "shift_45",
            "compound_stmt": "goto_46",
            "statement": "goto_47",
            "expression_stmt": "goto_48",
            "selection_stmt": "goto_49",
            "iteration_stmt": "goto_50",
            "return_stmt": "goto_51",
            "switch_stmt": "goto_52",
            "expression": "goto_53",
            "var": "goto_54",
            "simple_expression": "goto_55",
            "additive_expression": "goto_56",
            "term": "goto_57",
            "factor": "goto_58",
            "call": "goto_59",
            "}": "reduce_39",
            "case": "reduce_39",
            "default": "reduce_39"
        }
    }
}'''
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
        current_entry = self.parse_table2[str(number_before_push)][str(self.stack.get_top())]
        self.stack.push(parent)
        self.stack.push(current_entry)
        self.need_new_token = False

    def goto(self, number, _, __):
        self.stack.push(number)
