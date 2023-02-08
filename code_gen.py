from Parser.stack import Stack


# selection_stmt: "if" '(' expression ')' save statement "endif"  --> #jpf

# "if" '(' expression ')' save statement "else" jpf_save statement "endif" --> #jp

class IntermediateCodeGenerator:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.intermediate_code = ""
        self.current_index = 0
        self.var_index = 504
        self.semantic_stack = Stack()
        self.temp_values = dict()
        self.func_args = 0
        self.reference_stack = Stack()
        self.arr_vals = dict()
        self.states = {

        }
        self.actions = {
            '100': self.endfunc_action,  # not done
            '50': self.add_action,  # done
            '54': self.mult_action,  # done
            '68': self.save_action,  # done
            '69': self.jpf_save_action,  # done
            '31': self.jpf_action,  # done
            '32': self.jp_action,  # done
            '72': self.pid_action,  # done
            '42': self.assign_action,  # done
            '70': self.label_action,  # not done
            '33': self.while_action,  # not done
            '29': self.break_action,
            '71': self.switch_action,  # not done
            '80': self.case_condition_action,
            '104': self.finish_action,  # not done
            '105': self.out_action,  # not done
            '106': self.out_action,  # not done
            '73': self.declare_id_action,  # done
            '74': self.end_declare_func_action,  # done
            '6': self.end_declare_var_action,  # done
            '75': self.op_action,  # done
            '76': self.num_action,  # done
            '63': self.add_args_action,  # done
            '62': self.end_args_action,  # done
            '79': self.finish_exp_action,  # done
            '78': self.size_arr_action,  # done
            '45': self.arr_find_action,
            '81': self.fake_save_action,
            '36': self.switch_end_action,
            '82': self.jp_case_action,


            '46': self.relop
        }

    def code_gen(self, state, token=None):
        if state not in self.actions.keys():
            return
        param = {'token': token} if token is not None else {}
        action_function = self.actions[state]
        if state == '64':
            self.print_action(token)
        # noinspection PyArgumentList
        print('stack before ', self.semantic_stack)
        action_function(**param)
        print('current state is ', state)
        print('current action is ', action_function.__name__)
        print('stack is ', self.semantic_stack)
        print('code is:\n', self.intermediate_code)
        print('token is', token)
        print('------------------------------------------------------------------------------------------------------')

    # element [0] is address in symbol table
    # element [1] is name
    # element [2] is value
    # element [3] is variable address
    # element [4] is the type
    def num_action(self, token):
        self.symbol_table.append((len(self.symbol_table), '#NUM', int(token), self.var_index, 'num'))
        self.semantic_stack.push(self.var_index)
        self.var_index += 4
    def relop(self, token):
        self.condition_action(token)

    def finish_exp_action(self, token):
        self.semantic_stack.pop()

    def size_arr_action(self, token):
        size = int(token)
        address = self.semantic_stack.pop()
        arr = self.find_by_addr(address)
        index = arr[0]
        self.intermediate_code = "\n".join(self.intermediate_code.split('\n').pop(-1))
        self.current_index -= 1
        for i in range(size):
            self.symbol_table.append((index, arr[1] + '[' + str(i) + ']', 0, self.var_index, 'arr'))
            self.intermediate_code += str(self.current_index) + "\t(ASSIGN, #0," + str(self.var_index) + ",   )\n"
            self.var_index += 4
            self.current_index += 1

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

    def arr_find_action(self, token):
        print('Symbol_table:', self.symbol_table)
        index, start = self.semantic_stack.pop(2)
        index = self.find_operand(index)
        temp1 = self.var_index
        self.var_index += 4
        self.intermediate_code += str(self.current_index) + "\t(ADD, " + str(index[3])\
                                  + ", " + "#1" + "," + str(temp1) + " )\n"
        self.current_index += 1
        temp2 = self.var_index
        self.var_index += 4
        self.intermediate_code += str(self.current_index) + "\t(MULT, " + str(temp1)\
                                  + ", " + "#4" + "," + str(temp2) + " )\n"
        self.current_index += 1
        temp3 = self.var_index
        self.var_index += 4
        self.intermediate_code += str(self.current_index) + "\t(ADD, "+ str(temp2)\
                                  + ", " + '#' + str(start) + "," + str(temp3) + " )\n"
        self.current_index += 1
        self.semantic_stack.push(temp3)
        self.arr_vals[temp3] = temp3
    # initialize a variable by zero and give an address to it
    def declare_id_action(self, token):
        print(token)
        address = self.find_addr(token)
        try:
            index = self.symbol_table.index((address, token))
            self.symbol_table[index] = (address, token, 0, self.var_index, 'var')
            self.intermediate_code += str(self.current_index) + "\t(ASSIGN, #0," + str(self.var_index) + ",   )\n"
            self.var_index += 4
            self.current_index += 1
        except ValueError:
            return

    # TODO correct state numbers of actions after table update
    # TODO check if a function parameter can be another function return
    def end_args_action(self, token):
        self.semantic_stack.push(self.func_args)
        self.semantic_stack.push(self.current_index)
        func_address = self.semantic_stack.stack[-3 - self.func_args]
        if func_address == 500:
            self.semantic_stack.pop(2)
            for i in range(self.func_args):
                value = self.semantic_stack.pop()
                print(value)
                element = self.find_operand(value)
                print(element)
                if element[1] == '#NUM':
                    self.intermediate_code += str(self.current_index) + "\t(ASSIGN, " + str(element[3]) + "," + str(
                        value) + ",   )\n"
                    self.current_index += 1
                    self.intermediate_code += str(
                        self.current_index) + "\t(PRINT, " + str(value) + ", ,     )\n"
                else:
                    self.intermediate_code += str(
                        self.current_index) + "\t(PRINT, " + '@' + str(value) + ", ,     )\n"

                self.current_index += 1
            self.semantic_stack.pop()
        self.func_args = 0
        # because we pop values before ; this is a temp value
        self.semantic_stack.push(0)

    def end_declare_func_action(self, token):
        stack_address = self.semantic_stack.pop()
        element = self.find_by_addr(stack_address)
        index = self.symbol_table.index(element)
        self.symbol_table[index] = (element[0], element[1], None, element[3], 'func')
        print('FUCK')
        print(self.intermediate_code.split('\n').pop(-1))
        list_instruction = self.intermediate_code.split('\n')
        list_instruction.pop(-2)
        self.intermediate_code = "\n".join(list_instruction)
        self.current_index -= 1

    def end_declare_var_action(self, token):
        self.semantic_stack.pop()

    def op_action(self, token):
        self.semantic_stack.push(token)

    def condition_action(self, token):
        b, op, a = self.semantic_stack.pop(3)
        a = self.find_operand(a)
        b = self.find_operand(b)
        temp = self.var_index
        self.var_index += 4
        if op == '==':
            if a[2] == b[2]:
                value = 1
            else:
                value = 0
            self.intermediate_code += str(self.current_index) + "\t(EQ, " + str(a[3]) + ", " + str(b[3]) + "," + str(
                temp) + " )\n"
        else:
            if a[2] < b[2]:
                value = 1
            else:
                value = 0
            self.intermediate_code += str(self.current_index) + "\t(LT, " + str(a[3]) + ", " + str(b[3]) + "," + str(
                temp) + " )\n"

        self.temp_values[temp] = value
        self.semantic_stack.push(temp)
        self.current_index += 1

    def find_operand(self, address):
        if address in self.temp_values:
            temp = [None, None, self.temp_values[address], address, None]
            return temp
        elif address in self.arr_vals:
            temp = [None, None, self.arr_vals[address], '@' + str(address), None]
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
        self.func_args += 1

    def save_action(self, token):
        self.semantic_stack.push(self.current_index)
        self.current_index += 1

    def jpf_save_action(self, token):
        if token == 'default':
            self.current_index -= 1
        index, jump = self.semantic_stack.pop(2)
        current_index = self.current_index + 1
        if token == 'case':
            current_index -= 1
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(JPF, " + str(jump) + ", " + str(current_index) + ",  )\n")
        self.semantic_stack.push(self.current_index)
        self.current_index += 1
        self.intermediate_code = "\n".join(list_instructions)

    def jpf_action(self, token):
        index, jump = self.semantic_stack.pop(2)
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(JPF, " + str(jump) + ", " + str(self.current_index) + ",  )\n")
        self.intermediate_code = "\n".join(list_instructions)

    def jp_action(self, token):
        index = self.semantic_stack.pop(1)
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(JP, " + str(self.current_index) + ", ,  )\n")
        self.intermediate_code = "\n".join(list_instructions)

    def assign_action(self, token):
        value, var = self.semantic_stack.pop(2)
        value_holder = value
        value_element = self.find_operand(value)
        if value_element[4] == 'num':
            value = '#' + str(value_element[2])
        self.intermediate_code += str(self.current_index) + "\t(ASSIGN, " + str(value) + ", " + str(var) + ",   )\n"
        self.update_value(value_element[2], var)
        self.current_index += 1
        self.semantic_stack.push(value_holder)

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
                    if element[4] == 'num':
                        return [element[0], element[1], element[2], '#' + str(element[2]), element[4]]
                    else:
                        return element
            except IndexError:
                continue

    def print_action(self, token):
        num_args = self.semantic_stack.stack[-2]
        func_address = self.semantic_stack.stack[-3 - num_args]
        print(func_address)

    def label_action(self, token):
        self.semantic_stack.push(self.current_index)
        temp = self.var_index
        self.var_index += 4
        self.reference_stack.push((self.current_index, temp))
        self.temp_values[temp] = 0
        self.current_index += 1

    def while_action(self, token):
        index, last_reference = self.reference_stack.pop()
        self.temp_values[last_reference] = self.current_index + 1
        value = self.temp_values[last_reference]
        top, top_1, top_2 = self.semantic_stack.pop(3)
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(ASSIGN, #" + str(value) + ", " + str(last_reference) + ",  )")
        list_instructions.insert(top,
                                 str(top) + "\t(JPF, " + str(top_1) + ", " + str(self.current_index + 1) + ",  )\n")
        list_instructions.insert(self.current_index, str(self.current_index)
                                 + "\t(JP, " + str(top_2) + ",  " + ",  )\n")
        self.intermediate_code = "\n".join(list_instructions)
        self.current_index += 1

    def break_action(self, token):
        _, last_reference = self.reference_stack.get_top()
        self.intermediate_code += str(self.current_index) + "\t(JP, @" + str(last_reference) + ",  " + ",  )\n"
        self.current_index += 1

    def switch_action(self, token):
        self.label_action(token)
        # self.semantic_stack.push(self.current_index)

    def fake_save_action(self, token):
        temp = self.var_index
        self.var_index += 4
        self.semantic_stack.push('#0')
        self.semantic_stack.push(self.current_index)
        self.current_index += 1

    def case_condition_action(self, token):
        temp = self.var_index
        self.var_index += 4
        expression_result = self.semantic_stack.get_top()
        self.intermediate_code += str(self.current_index - 1) + f"\t(EQ, #{token}," + str(
            expression_result) + f", {temp})\n"
        self.semantic_stack.push(temp)

    def finish_action(self, token):
        pass

    def out_action(self, token):
        pass

    def endfunc_action(self, token):
        pass

    def relop_action(self, token):
        pass

    def switch_end_action(self, token):
        index, last_reference = self.reference_stack.pop()
        self.temp_values[last_reference] = self.current_index + 1
        value = self.temp_values[last_reference]
        # top, top_1 = self.semantic_stack.pop(2)
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(ASSIGN, #" + str(value) + ", " + str(last_reference) + ",  )")
        self.intermediate_code = "\n".join(list_instructions)
        self.semantic_stack.pop()
        # self.current_index += 1

    def jp_case_action(self, token):
        index, jump = self.semantic_stack.pop(2)
        list_instructions = self.intermediate_code.split('\n')
        list_instructions.insert(index,
                                 str(index) + "\t(JPF, " + str(jump) + ", " + str(self.current_index) + ",  )\n")
        self.intermediate_code = "\n".join(list_instructions)
        self.current_index += 1
