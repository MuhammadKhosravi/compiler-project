class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self, number_of_pops=1):
        list_of_popped = []
        for _ in range(number_of_pops):
            list_of_popped.append(self.stack.pop())
        return list_of_popped[0] if number_of_pops == 1 else list_of_popped

    def get_top(self):
        return self.stack[-1]

    def get_last_state(self):
        return self.stack[-3]

    def __str__(self):
        return str(self.stack)
