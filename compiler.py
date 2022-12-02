from scanner import Scanner
# Set this variable to empty string before submitting the answer
INPUT_PATH_PREFIX = "./test/T07/"

# INPUT_PATH_PREFIX = ""

if __name__ == "__main__":
    # code driver
    with open(INPUT_PATH_PREFIX+'input.txt', 'r') as file:
        input_string = file.readlines()
        scanner = Scanner(input_string)
        #This line is for test purposes
        scanner.get_next_token()

