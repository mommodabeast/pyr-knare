import re

def error_checker(expression):
    result1 = re.search(r"[+-]?-\d+.\d+ -\d+|-\d+.\d+ \d+|-\d+ -\d+|-\d+.\d+ \d+|-\d+ \d+|\d+.\d+ -\d+|\d+ -\d+|\d+ \d+" ,expression)
    if result1 == None:
        print("Right!")
    else:
        print("Wrong!")
 #   result2 = re.search(r"[+-]?[+/-][-/+]|[+/-][+/-]")
