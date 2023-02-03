from IO.File import TextFile
from scanner import Scanner
from Language.Programming_language import CMinus
from my_parser import Parser
# Set this variable to empty string before submitting the answer
INPUT_PATH_PREFIX = "testcases/T1/"

#INPUT_PATH_PREFIX = ""

# Muhammad Khosravi 99105407
# Arash Fattani Farshbaf 99101965

if __name__ == "__main__":
    # code driver
    address = INPUT_PATH_PREFIX + 'input.txt'
    language = CMinus()
    code = TextFile(address)
    scanner = Scanner(code.access(), language)
    parser = Parser(scanner)
    parser.parse()
