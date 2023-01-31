class TextFile:
    def __init__(self, address):
        self.address = address

    def access(self):
        with open(self.address, 'r') as file:
            input_string = file.readlines()
        if input_string[-1][-1] != '\n':
            input_string[-1] = input_string[-1] + '\n'
        return input_string
