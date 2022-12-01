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
        for char, state in zip(self.characters, self.next_states):
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
# TODO when input ends report EOF to the scanner
# TODO between some tokens there must be whitespace 125d
class Scanner:

    def __init__(self, input_text):
        self.input_text = input_text
        self.states = self.build_states()

    def build_states(self):
        NUMBER_OF_STATES = 17
        states = [State(i) for i in range(NUMBER_OF_STATES)]
        digit = "0123456789"
        letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        symbol = ";:,[](){}+-*=<"
        whitesapce = " \r\r\v\f"
        EOF = ''
        characters = [digit, letter, symbol, '=', whitesapce, '*', '/', '\n', '#', EOF]
        states_transition = [{0: 1, 1: 1, 3: 3},  # for digit
                             {0: 3, 3: 3},  # for letter
                             {0: 5},  # for symbol
                             {0: 6, 6: 8},  # for =
                             {0: 16},  # for whitespace
                             {9: 13, 13: 14},  # for *
                             {0: 9, 9: 11, 14: 15},  # for /
                             {11: 12},  # for \n
                             {1: 2, 3: 4, 6: 7, 13: 13, 11: 11, 9: 10},  # for other
                             {11: 12}]  # for EOF
        for char, states_tran in zip(characters, states_transition):
            for first, second in states_tran.items():
                states[first].add_transition(states[second], char)
        final_state_to_token_type = {2: "NUM", 4: "ID", 5: "SYMBOL", 7: "SYMBOL",
                                     8: "SYMBOL", 16: "WHITESPACE", 10: "SYMBOL", 12: "COMMENT", 15: "COMMENT"}
        others = [2, 4, 7, 10, 12]
        for state_number in final_state_to_token_type.keys():
            states[state_number].set_accepting(
                final_state_to_token_type[state_number])
            if state_number in others:
                states[state_number].go_back = True
        return states

    def get_next_token(self):
        current_state = self.states[0]
        current_token = ""
        index = 0
        result = []
        while index < len(self.input_text):
            if self.input_text[index] == '':
                break
            for chars, state in current_state.transitions:
                if self.input_text[index] in chars or chars == '#':
                    current_state = state
                    if current_state.go_back:
                        index -= 1
                    else:
                        current_token += self.input_text[index]
                    break
            index += 1
            if current_state.is_accepting:
                result.append((current_token, current_state.token_type))
                current_state = self.states[0]
                current_token = ""

        print(result)
