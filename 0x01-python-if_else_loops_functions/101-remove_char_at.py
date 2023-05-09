#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    j = 0
    while j < len(str):
        if j == n:
            j = j + 1
        result += str[j]
        j = j + 1
    return result
