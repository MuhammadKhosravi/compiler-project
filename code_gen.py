from Parser.stack import Stack


# selection_stmt: "if" '(' expression ')' save statement "endif"  --> #jpf

# "if" '(' expression ')' save statement "else" jpf_save statement "endif" --> #jp

class IntermediateCodeGenerator:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.intermediate_code = ""
        self.current_index = 0
        self.var_index = 500
        self.semantic_stack = Stack()
        self.states = {

        }
        self.actions = {
            '9': self.endfunc_action,
            '50': self.add_action,
            '54': self.mult_action,
            '67': self.save_action,
            '70': self.jpf_save_action,
            '31': self.jpf_action,
            '32': self.jp_action,
            '71': self.pid_action,
            '42': self.assign_action,
            '68': self.print_action,
            '69': self.label_action,
            '33': self.while_action,
            '75': self.switch_action,
            '36': self.finish_action,
            '40': self.out_action,
            '39': self.out_action,
            '46': self.relop_action,
            '72': self.declare_id_action,
            '73': self.end_declare_action
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

    # TODO delete value part of symbol table for functions
    # initialize a variable by zero and give an address to it
    def declare_id_action(self, token):
        address = self.find_addr(token)
        try:
            index = self.symbol_table.index((address, token))
            self.symbol_table[index] = (address, token, 0, self.var_index)
            self.intermediate_code += str(self.current_index) + "\t(ASSIGN, #0," + str(self.var_index) + ",   )\n"
            self.var_index += 4
            self.current_index += 1
        except ValueError:
            return

    def end_declare_action(self, token):
        self.semantic_stack.pop()


    def mult_action(self, token):
        print(token)
        print('HOYYY')

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
        address = self.find_var_addr(token)
        self.semantic_stack.push(address)

    # element [0] is address in symbol table
    # element [1] is name
    # element [2] is value
    # element [3] is variable address
    def find_addr(self, current_token):
        for element in self.symbol_table:
            if element[1] == current_token:
                return element[0]

    def find_var_addr(self, current_token):
        for element in self.symbol_table:
            if element[1] == current_token:
                return element[3]

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
