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
        self.temp_values = dict()
        self.states = {

        }
        self.actions = {
            '9': self.endfunc_action,  # not done
            '50': self.add_action,  # done
            '54': self.mult_action,  # done
            '67': self.save_action,  # not done
            '70': self.jpf_save_action,  # not done
            '31': self.jpf_action,  # not done
            '32': self.jp_action,  # not done
            '74': self.pid_action,  # done
            '42': self.assign_action,  # done
            '64': self.print_action,  # not done
            '69': self.label_action,  # not done
            '33': self.while_action,  # not done
            '65': self.switch_action,  # not done
            '36': self.finish_action,  # not done
            '40': self.out_action,  # not done
            '39': self.out_action,  # not done
            '46': self.relop_action,  # not done
            '75': self.declare_id_action,       #done
            '76': self.end_declare_func_action, #done
            '6': self.end_declare_var_action,   #done
            '7': self.end_declare_var_action,   #done
            '77': self.op_action,               #done
            '78': self.num_action,              #done
            '63': self.add_args_action     #not done
        }

    def code_gen(self, state, token=None):
        if state not in self.actions.keys():
            return
        param = {'token': token} if token is not None else {}
        action_function = self.actions[state]
        # noinspection PyArgumentList
        action_function(**param)

    # element [0] is address in symbol table
    # element [1] is name
    # element [2] is value
    # element [3] is variable address
    # element [4] is the type
    def num_action(self, token):
        self.symbol_table.append((len(self.symbol_table), '#NUM', int(token), self.var_index, 'num'))
        self.semantic_stack.push(self.var_index)
        self.var_index += 4

    def add_action(self, token):
        B, op, A = self.semantic_stack.pop(3)
        A = self.find_operand(A)
        B = self.find_operand(B)
        temp = self.var_index
        self.var_index += 4
        if op == "+":
            res = A[2] + B[2]
            self.intermediate_code += str(self.current_index) + "\t(ADD, " + str(A[3]) + ", " + str(B[3]) + "," + str(
                temp) + " )\n"
        else:
            res = A[2] - B[2]
            self.intermediate_code += str(self.current_index) + "\t(SUB, " + str(A[3]) + ", " + str(B[3]) + "," + str(
                temp) + " )\n"
        self.temp_values[temp] = int(res)
        self.semantic_stack.push(temp)
        self.current_index += 1

    # TODO eliminate giving value to the function from intermediate code
    # initialize a variable by zero and give an address to it
    def declare_id_action(self, token):
        address = self.find_addr(token)
        try:
            index = self.symbol_table.index((address, token))
            self.symbol_table[index] = (address, token, 0, self.var_index, 'var')
            self.intermediate_code += str(self.current_index) + "\t(ASSIGN, #0," + str(self.var_index) + ",   )\n"
            self.var_index += 4
            self.current_index += 1
        except ValueError:
            return

    def end_declare_func_action(self, token):
        stack_address = self.semantic_stack.pop()
        element = self.find_by_addr(stack_address)
        index = self.symbol_table.index(element)
        self.symbol_table[index] = (element[0], element[1], None, element[3], 'func')

    def end_declare_var_action(self, token):
        self.semantic_stack.pop()

    def op_action(self, token):
        self.semantic_stack.push(token)

    def find_operand(self, address):
        if address in self.temp_values:
            temp = [None, None, self.temp_values[address], address, None]
            return temp
        else:
            return self.find_by_addr(address)

    def mult_action(self, token):
        B, op, A = self.semantic_stack.pop(3)
        A = self.find_operand(A)
        B = self.find_operand(B)
        temp = self.var_index
        self.var_index += 4
        if op == "*":
            res = A[2] * B[2]
            self.intermediate_code += str(self.current_index) + "\t(MULT, " + str(A[3]) + ", " + str(B[3]) + "," + str(
                temp) + " )\n"
        else:
            res = A[2] // B[2]
            self.intermediate_code += str(self.current_index) + "\t(DIV, " + str(A[3]) + ", " + str(B[3]) + "," + str(
                temp) + " )\n"
        self.temp_values[temp] = int(res)
        self.semantic_stack.push(temp)
        self.current_index += 1

    def add_args_action(self, token):
        print(token)

    def save_action(self, token):
        pass

    def jpf_save_action(self, token):
        pass

    def jpf_action(self, token):
        pass

    def jp_action(self, token):
        pass

    def assign_action(self, token):
        value, var = self.semantic_stack.pop(2)
        value_element = self.find_operand(value)
        if value_element[4] == 'num':
            value = '#' + str(value_element[2])
        self.intermediate_code += str(self.current_index) + "\t(ASSIGN, " + str(value) + "," + str(var) + ",   )\n"
        self.update_value(value_element[2], var)
        self.current_index += 1

    def update_value(self, value, var):
        element = self.find_operand(var)
        try:
            index = self.symbol_table.index(element)
            self.symbol_table[index] = (element[0], element[1], value, element[3], element[4])
        except ValueError:
            self.temp_values[var] = value

    def pid_action(self, token):
        address = self.find_var_addr(token)
        self.semantic_stack.push(address)

    # element [0] is address in symbol table
    # element [1] is name
    # element [2] is value
    # element [3] is variable address
    # element [4] is the type
    def find_addr(self, current_token):
        for element in self.symbol_table:
            if element[1] == current_token:
                return element[0]

    def find_var_addr(self, current_token):
        for element in self.symbol_table:
            if element[1] == current_token:
                return element[3]

    def find_by_addr(self, address_stack):
        for element in self.symbol_table:
            try:
                if element[3] == address_stack:
                    return element
            except IndexError:
                continue

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
