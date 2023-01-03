class TextFile:
    def __init__(self, address):
        self.address = address

    def access(self):
        with open(self.address, 'r') as file:
            input_string = file.readlines()
        return input_string
