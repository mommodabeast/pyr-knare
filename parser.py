import re

def error_checker():
    pass

def is_number(string):
    # Works for integer numbers and numbers with decimal parts (real numbers!).
    if re.match(r"[+-]?-\d+.\d+|-\d+|\d+.\d+|\d+", string) != None:
        return True
    else:
        return False

def parser(string):
    # Return a tuple containing integers, floating-point numbers and strings (operators, parentheses or functions).

    string = string.replace(",", ".")

    # Get numbers and operators
    # Note: + and - cannot be next to each other or else python will raise an error. 
    matched_substrings = re.findall(r"[+-]?-\d+.\d+|-\d+|\d+.\d+|\d+|[+*-/]", string)
    error_code = error_checker()
    if error_code != None:
        return error_code

    parsed_string = [float(string) if is_number(string) else string for string in matched_substrings]
    
    return parsed_string
    
   

if __name__ == "__main__":
    expression = parser("1 + 1,1223+2   / 3 * 4 + -1,2 - 1")
    print(expression)