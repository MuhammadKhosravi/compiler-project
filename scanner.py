class Scanner:
    def __init__(self, input_text, language):
        self.input_text = input_text
        self.language = language
        self.states = language.states
        self.symbol_table = [(i, language.KEYWORDS[i]) for i in range(len(language.KEYWORDS))]
        self.errors = []
        self.current_line_index = (0, 0)
        self.current_comment_start = 0
        self.all_tokens = []

    def add_to_symbol_table(self, keyword_or_identifier):
        if keyword_or_identifier not in [x[1] for x in self.symbol_table]:
            self.symbol_table.append((len(self.symbol_table), keyword_or_identifier))

    def add_error(self, line_number, error_message, token, trash):
        if len(self.errors) != 0 and int(self.errors[-1].split('.')[0]) == line_number:
            self.errors[-1] += f" ({token + trash}, {error_message})"
        else:
            self.errors.append(f"{line_number}.\t({token + trash}, {error_message})")

    def is_number_invalid(self, current_token):
        return len(current_token) != 0 and current_token[0] in self.language.characters["digit"]

    # why we have current comment start because there can't be another token between comments
    def get_next_token(self):
        current_state = self.states[0]
        current_token = ""
        current_line_index, index = self.current_line_index
        try:
            for line_index in range(current_line_index, len(self.input_text)):
                if index == len(self.input_text[line_index]) - 1:
                    if line_index == len(self.input_text) - 1:
                        if current_state.number == 13:
                            self.handle_adding_error(current_token, self.current_comment_start, False, True, '',
                                                     self.current_comment_start)
                        raise IndexError
                    line_index += 1
                    index = 0
                while index < len(self.input_text[line_index]):
                    current_char = self.input_text[line_index][index]
                    if current_char == '':
                        break
                    trash = ""
                    for chars, state in current_state.transitions:
                        if current_char in chars or chars == '#':
                            if self.is_number_invalid(current_token) and current_char in \
                                    self.language.characters["letter"]:
                                trash += current_char
                                continue
                            current_state = state
                            if current_state.go_back:
                                if current_state.number in [2, 4,
                                                            7] and current_char not in self.language.Allowed_characters:
                                    trash = current_char
                                    continue
                                else:
                                    index -= 1
                            else:
                                current_token += self.input_text[line_index][index]

                            break
                    else:
                        trash = trash if trash else current_char
                        current_state, current_token = self.handle_adding_error(current_token, line_index + 1, False,
                                                                                False,
                                                                                trash, self.current_comment_start)
                    index += 1
                    if current_state.is_accepting:
                        if current_state.number == 19:
                            current_state, current_token = self.handle_adding_error(current_token, line_index + 1, True,
                                                                                    False, trash,
                                                                                    self.current_comment_start)
                        else:
                            if current_state.token_type != 'COMMENT':
                                current_token = self.handle_adding_token(current_state, current_token,
                                                                         self.all_tokens)
                                if current_token is None:
                                    current_state = self.states[0]
                                    current_token = ""
                                    continue
                                self.current_line_index = (line_index, index)
                                return current_token
                            elif current_token.startswith("//"):
                                current_state = self.states[0]
                            elif current_token.endswith("*/"):
                                current_token = ''
                                current_state = self.states[0]
                index = 0
                if current_state.number == 13 and self.current_comment_start == 0:
                    self.current_comment_start = line_index + 1
            return '$'
        except IndexError as I:
            return '$'

    def handle_adding_error(self, current_token, line_index, is_bad, unclosed, trash, comment_start):
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
            if current_token.startswith("/*") and current_token.endswith("*"):
                self.add_error(comment_start, "Unclosed comment", current_token[:7] + "...", trash)
            else:
                self.add_error(line_index, "Invalid input", current_token, trash)
        current_state = self.states[0]
        current_token = ""
        return current_state, current_token

    def handle_adding_token(self, current_state, current_token, result_per_line):
        token_type = current_state.token_type
        if current_state.token_type == "ID":
            self.add_to_symbol_table(current_token)
            if current_token in self.language.KEYWORDS:
                token_type = "KEYWORD"
        if token_type != "WHITESPACE":
            result_per_line.append((token_type, current_token))
            return current_token
