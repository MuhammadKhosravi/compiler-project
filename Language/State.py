class State:
    def __init__(self, number):
        self.number = number
        self.transitions = []
        self.token_type = None
        self.is_accepting = False
        self.go_back = False

    def add_transition(self, next_state, character):
        self.transitions.append((character, next_state))

    def set_accepting(self, token_type):
        self.is_accepting = True
        self.token_type = token_type
