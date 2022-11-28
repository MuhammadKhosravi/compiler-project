class State:
    def __init__(self, number):
        self.number = number
        self.next_states = list()
        self.characters = list()
        self.is_accepting = False

    def transition(self, next_state, character):
        self.next_states.append(next_state)
        self.characters.append(character)

    def set_accepting(self):
        self.is_accepting = True

    def __str__(self):
        description = "state " + str(self.number) + "\ntransitions: \n"
        for char, state in zip(self.characters, self.next_states):
            description += "with " + char + " go to the state " + str(state.number) + "\n"
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
        states = list()
        for i in range(17):
            states.append(State(i))
        characters = ['d', 'l', 's', '=', 'w', '*', '/', 'n', '#', 'f']
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
                states[first].transition(states[second], char)
        final_states = [2, 4, 5, 7, 8, 16, 10, 12, 15]
        for st in final_states:
            states[st].set_accepting()
        return states

    def get_next_token(self):
        current_state = self.states[0]
        for char in self.input_text:
            # TODO check if char matches a state and change current state to that
            pass
