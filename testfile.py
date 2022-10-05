import re

def parser(string):
    result = re.findall("\d+", string)
    print(result)

if __name__ == "__main__":
    parser("234 324 55 1 0 abc")