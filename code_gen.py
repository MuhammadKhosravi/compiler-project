from Parser.stack import Stack


class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = ""
        self.semantic_stack = Stack()
        self.actions = {
            'add': self.add_action,
            'mult': self.mult_action,
            'save': self.save_action,
            'jpf_save': self.jpf_save_action,
            'jpf': self.jpf_action,
            'jp': self.jp_action,
            'pid': self.pid_action,
            'assign': self.assign_action,
            'print': self.print_action,
            'label': self.label_action,
            'while': self.while_action,
            'switch': self.switch_action,
            'finish': self.finish_action,
            'out': self.out_action,
        }

    def code_gen(self, action_symbol, token=None):
        param = {'token': token} if token is not None else {}
        action_function = self.actions[action_symbol]
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
