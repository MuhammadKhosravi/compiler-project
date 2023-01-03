from scanner import Scanner
from IO.File import TextFile
from Language.Programming_language import *
from parser import Parser

# Set this variable to empty string before submitting the answer
INPUT_PATH_PREFIX = "./test/T01/"

# INPUT_PATH_PREFIX = ""

# Muhammad Khosravi 99105407
# Arash Fattani Farshbaf 99101965
if __name__ == "__main__":
    # code driver
    address = INPUT_PATH_PREFIX + 'input.txt'
    language = CMinus()
    code = TextFile(address)
    scanner = Scanner(code.access(), language)
    # index = 0
    # while True:
    #     index += 1
    #     token = scanner.get_next_token()
    #     print(token)
    #     if token == '$':
    #         break
    #     if index == 1000:
    #         break
    # print(scanner.symbol_table)
    # print(scanner.errors)
    parser = Parser()

