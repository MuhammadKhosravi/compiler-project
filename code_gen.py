from Parser.stack import Stack

#selection_stmt: "if" '(' expression ')' save statement "endif"  --> #jpf

#"if" '(' expression ')' save statement "else" jpf_save statement "endif" --> #jp

class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = ""
        self.semantic_stack = Stack()
        self.actions = {
            50: self.add_action,
            54: self.mult_action,
            69: self.save_action,
            70: self.jpf_save_action,
            31: self.jpf_action,
            32: self.jp_action,
            73: self.pid_action,
            42: self.assign_action,
            68: self.print_action,
            71: self.label_action,
            33: self.while_action,
            72: self.switch_action,
            36: self.finish_action,
            40: self.out_action,
            39: self.out_action,
        }
        self.states = {

        }

    def code_gen(self, state, token=None):
        param = {'token': token} if token is not None else {}
        action_function = self.actions[state]
        # noinspection PyArgumentList
        action_function(**param)

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

    def pid_action(self, token):
        pass

    def print_action(self, token):
        pass

    def label_action(self):
        pass

    def while_action(self):
        pass

    def switch_action(self):
        pass

    def finish_action(self):
        pass

    def out_action(self):
        pass


if __name__ == '__main__':
    cg = IntermediateCodeGenerator()
    cg.code_gen('pid', 'salam')
