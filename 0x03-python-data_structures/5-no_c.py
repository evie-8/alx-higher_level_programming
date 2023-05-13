#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        result += i
    return result
