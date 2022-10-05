import re

def is_number(string):
    if re.match(r"[+-]?\d+.\d+|\d+", string) != None:
        return True
    else:
        return False

def parser(string):
    # Return a tuple containing integers, floating-point numbers and strings (operators, parentheses or functions).


    # Get numbers and operators
    # Note: + and - cannot be next to each other or else python will raise an error. 
    matched_strings = re.findall(r"[+-]?\d+.\d+|\d+|[+*-/]", string)
    numbers = [float(string) for string in matched_strings if is_number(string)]
    print(numbers)
    
    

if __name__ == "__main__":
    parser("1 av bddf+  dgdfgdf3.3 4444a 3 3 3 3 3  3 3 3  33 3 3 33 3 ")