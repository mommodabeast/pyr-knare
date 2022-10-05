import re

def parser(string):

    numbers = re.findall(r"[+-]?\d+.\d+|\d+,\d+|\d+", string)
    print(numbers)

if __name__ == "__main__":
    parser("234.4 32,4 + 55 - 1 ? 0 abc")