import re


class State:
    def __init__(self, number):
        self.number = number
        self.transitions = []
        # self.next_states = []
        # self.characters = []
        self.token_type = None
        self.is_accepting = False
        self.go_back = False

    def add_transition(self, next_state, character):
        self.transitions.append((character, next_state))
        # self.next_states.append(next_state)
        # self.characters.append(character)

    def set_accepting(self, token_type):
        self.is_accepting = True
        self.token_type = token_type

    def __str__(self):
        description = "state " + str(self.number) + "\ntransitions: \n"
        for char, state in self.transitions:
            description += "with " + char + \
                           " go to the state " + str(state.number) + "\n"
        if self.is_accepting:
            description += "it is final state"
        return description

    def __repr__(self):
        return str(self)


# d is used to represent digit
# l is used to represent letter
# s is used to represent symbol
# = is used to represent =
# w is used to represent whitespace
# * is used to represent *
# /  is used to represent
# n is used to represent \n
# # is used to represent other
# f is used to represent EOF
KEYWORDS = ["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return", "endif"]
digit = "0123456789"
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = ";:,[](){}+-<"
whitesapce = " \r\r\v\f\n\t"
EOF = ''


class Scanner:

    def __init__(self, input_text):
        self.input_text = input_text
        self.states = self.build_states()
        self.symbol_table = []
        self.symbol_table_str = []
        for key_word in KEYWORDS:
            self.add_to_symbol_table(key_word)
        self.errors = []

    def add_to_symbol_table(self, keyword_or_identifier):
        first_time = True
        for _, idd in self.symbol_table:
            if idd == keyword_or_identifier:
                first_time = False
        if first_time:
            self.symbol_table.append((len(self.symbol_table), keyword_or_identifier))
            self.symbol_table_str.append(f"{len(self.symbol_table)}: {keyword_or_identifier}")

    def build_states(self):
        NUMBER_OF_STATES = 20
        states = [State(i) for i in range(NUMBER_OF_STATES)]
        characters = [digit, letter, symbol, '=', whitesapce, '*', '/', '\n', '#', EOF]
        states_transition = [{0: 1, 1: 1, 3: 3},  # for digit
                             {0: 3, 3: 3},  # for letter
                             {0: 5},  # for symbol
                             {0: 6, 6: 8},  # for =
                             {0: 16},  # for whitespace
                             {9: 13, 13: 14, 0: 17},  # for *
                             {0: 9, 9: 11, 14: 15, 17: 19},  # for /
                             {11: 12},  # for \n
                             {1: 2, 3: 4, 6: 7, 13: 13, 11: 11, 9: 10, 17: 18},  # for other
                             {11: 12}]  # for EOF
        for char, states_tran in zip(characters, states_transition):
            for first, second in states_tran.items():
                states[first].add_transition(states[second], char)
        final_state_to_token_type = {2: "NUM", 4: "ID", 5: "SYMBOL", 7: "SYMBOL",
                                     8: "SYMBOL", 16: "WHITESPACE", 10: "SYMBOL", 12: "COMMENT", 15: "COMMENT",
                                     18: "SYMBOL", 19: "BAD_COMMENT"}
        others = [2, 4, 7, 10, 12, 18]
        for state_number in final_state_to_token_type.keys():
            states[state_number].set_accepting(
                final_state_to_token_type[state_number])
            if state_number in others:
                states[state_number].go_back = True
        return states

    def write_results_to_file(self, tokens, symbol_table, errors):
        tokens.append('')
        with open("tokens.txt", "w") as file:
            file.write("\n".join(tokens))
        with open("symbol_table.txt", "w") as file:
            file.write('\n'.join(symbol_table))
        with open('lexical_errors.txt', "w") as file:
            if len(errors) > 0:
                file.write('\n'.join(errors))
            else:
                file.write("There is no lexical error.")

    def add_error(self, line_number, error_message, token, trash):
        if len(self.errors) != 0 and int(self.errors[-1].split('.')[0]) == line_number:
            self.errors[-1] += f" ({token + trash}, {error_message})"
        else:
            self.errors.append(f"{line_number}.{' ': ^3}({token + trash}, {error_message})")

    def is_number_invalid(self, current_token):
        return re.search(r"^\d", current_token) is not None

    def get_next_token(self):
        current_state = self.states[0]
        current_token = ""
        total_result = []
        comment_start = 0
        for line_index in range(len(self.input_text)):
            index = 0
            result_per_line = []
            while index < len(self.input_text[line_index]):
                current_char = self.input_text[line_index][index]
                if current_char == '':
                    break
                trash = ""
                if line_index == 5:
                    print('fuck')
                for chars, state in current_state.transitions:
                    if current_char in chars or chars == '#':
                        if self.is_number_invalid(current_token) and current_char in letter:
                            # index += 1
                            trash += current_char
                            continue
                        current_state = state
                        if current_state.go_back:
                            index -= 1
                        else:
                            current_token += self.input_text[line_index][index]
                        break
                else:
                    trash = trash if trash else current_char
                    current_state, current_token = self.handle_adding_error(current_token, line_index + 1, False, False, trash)
                index += 1
                if current_state.is_accepting:
                    if current_state.number == 19:
                        current_state, current_token = self.handle_adding_error(current_token, line_index + 1, True,
                                                                                False, trash)
                    else:
                        current_state, current_token = self.handle_adding_token(current_state, current_token,
                                                                                result_per_line)
            if current_state.number == 13:
                comment_start = line_index
            str_result_line = ""
            for token in result_per_line:
                str_result_line += '(' + token[0] + ', ' + token[1] + ') '
            if str_result_line != '':
                total_result.append(f"{line_index + 1}.\t{str_result_line}")
        if current_state.number == 13:
            self.handle_adding_error(current_token, comment_start, False, True)
        self.write_results_to_file(total_result, self.symbol_table_str, self.errors)

    def handle_adding_error(self, current_token, line_index, is_bad, unclosed, trash):
        if self.is_number_invalid(current_token):
            self.add_error(line_index, "Invalid number", current_token, trash)
        elif is_bad:
            self.add_error(line_index, "Unmatched comment", current_token, trash)
        elif unclosed:
            if len(current_token) < 7:
                self.add_error(line_index, "Unclosed comment", current_token, trash)
            else:
                self.add_error(line_index, "Unclosed comment", current_token[:7] + "...", trash)
        else:
            self.add_error(line_index, "Invalid input", current_token, trash)
        current_state = self.states[0]
        current_token = ""
        return current_state, current_token

    def handle_adding_token(self, current_state, current_token, result_per_line):
        token_type = current_state.token_type
        if current_state.token_type == "ID":
            self.add_to_symbol_table(current_token)
            if current_token in KEYWORDS:
                token_type = "KEYWORD"
        if token_type != "WHITESPACE":
            result_per_line.append((token_type, current_token))
        current_state = self.states[0]
        current_token = ""
        return current_state, current_token
