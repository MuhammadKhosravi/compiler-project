from Parser.stack import Stack

#selection_stmt: "if" '(' expression ')' save statement "endif"  --> #jpf

#"if" '(' expression ')' save statement "else" jpf_save statement "endif" --> #jp

class IntermediateCodeGenerator:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.intermediate_code = ""
        self.current_index = 0
        self.semantic_stack = Stack()
        self.states = {

        }
        self.actions = {
            '9': self.endfunc_action,
            '50': self.add_action,
            '54': self.mult_action,
            '69': self.save_action,
            '70': self.jpf_save_action,
            '31': self.jpf_action,
            '32': self.jp_action,
            '73': self.pid_action,
            '42': self.assign_action,
            '68': self.print_action,
            '71': self.label_action,
            '33': self.while_action,
            '72': self.switch_action,
            '36': self.finish_action,
            '40': self.out_action,
            '39': self.out_action,
            '46': self.relop_action,
        }

    def code_gen(self, state, token=None):
        if state not in self.actions.keys():
            return
        param = {'token': token} if token is not None else {}
        action_function = self.actions[state]
        # noinspection PyArgumentList
        action_function(**param)


    def add_action(self, token):
        pass

    def mult_action(self, token):
        pass

    def save_action(self, token):
        pass

    def jpf_save_action(self, token):
        pass

    def jpf_action(self, token):
        pass

    def jp_action(self, token):
        pass

    def assign_action(self, token):
        pass

    def pid_action(self, token):
        pass

    def print_action(self, token):
        pass

    def label_action(self, token):
        pass

    def while_action(self, token):
        pass

    def switch_action(self, token):
        pass

    def finish_action(self, token):
        pass

    def out_action(self, token):
        pass

    def endfunc_action(self, token):
        pass

    def relop_action(self, token):
        pass


if __name__ == '__main__':
    cg = IntermediateCodeGenerator()
    cg.code_gen('pid', 'salam')
