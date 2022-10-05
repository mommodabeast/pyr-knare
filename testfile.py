import re

def parser(string):
    # Return a tuple containing integers, floating-point numbers and strings (operators, parentheses or functions).


    # Get numbers and operators
    # Note: + and - cannot be next to each other or else python will raise an error. 
    numbers = re.findall(r"[+-]?\d+.\d+|\d+,\d+|\d+|[+*-/]", string)
    return numbers

if __name__ == "__main__":
    parser("1 av bddf+  dgdfgdf3.3 4444a")