class State:
    def __init__(self, number):
        self.number = number
        self.next_state = None

    def set_next_state(self, next_state):
        self.next_state = next_state
        
class Scanner:
    def __init__(self, input_text):
        self.input_text = input_text
        self.states = self.build_states()

    def build_states(self):
        # TODO build DFA using State objects (manually)
        pass
    def get_next_token(self):
        current_state = self.states[0]
        for char in self.input_text:
            # TODO check if char matches a state and change current state to that
            pass