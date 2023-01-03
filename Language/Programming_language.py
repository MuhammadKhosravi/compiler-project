from Language.State import State


class ProgrammingLanguage:

    def __init__(self):
        self.states = None
        self.characters = {"digit": "0123456789", "letter": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                           "whitespace": " \r\r\v\f\n\t", "EOF": ''}


class CMinus(ProgrammingLanguage):
    # # is used to represent other

    def __init__(self):
        super().__init__()
        self.KEYWORDS = ["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return", "endif"]
        self.symbol = ";:,[](){}+-<"
        self.Allowed_characters = self.characters["digit"] + self.characters["letter"] + \
                                  self.symbol + self.characters["whitespace"] + self.characters["EOF"] + \
                                  "=*/"
        self.states = self.build_states()

    def build_states(self):
        NUMBER_OF_STATES = 20
        states = [State(i) for i in range(NUMBER_OF_STATES)]
        characters = [self.characters["digit"], self.characters["letter"],
                      self.symbol, '=', self.characters["whitespace"], '*', '/', '\n', '#',
                      self.characters["EOF"]]
        states_transition = [{0: 1, 1: 1, 3: 3},  # for digit
                             {0: 3, 3: 3},  # for letter
                             {0: 5},  # for symbol
                             {0: 6, 6: 8},  # for =
                             {0: 16},  # for whitespace
                             {9: 13, 13: 14, 0: 17},  # for *
                             {0: 9, 9: 11, 14: 15, 17: 19},  # for /
                             {11: 12},  # for \n
                             {1: 2, 3: 4, 6: 7, 13: 13, 11: 11, 9: 10, 17: 18, 14: 13},  # for other
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
