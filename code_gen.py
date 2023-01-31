class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = ""

    def code_gen(self, action_symbol):
        if action_symbol == 'add':
            self.add_action()
        elif action_symbol == 'mult':
            self.mult_action()
        elif action_symbol == 'save':
            self.save_action()
        elif action_symbol == 'jpf_save':
            self.jpf_save_action()
        elif action_symbol == 'jpf':
            self.jpf_action()
        elif action_symbol == 'jp':
            self.jp_action()
        elif action_symbol == 'id':
            self.id_action()
        elif action_symbol == 'assign':
            self.assign_action()

    def add_action(self):
        pass

    def mult_action(self):
        pass

    def save_action(self):
        pass

    def jpf_save_action(self):
        pass

    def jpf_action(self):
        pass

    def jp_action(self):
        pass

    def assign_action(self):
        pass

    def id_action(self):
        pass
