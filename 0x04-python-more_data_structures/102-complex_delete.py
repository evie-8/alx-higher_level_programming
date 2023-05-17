#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    s = []
    for k, v in a_dictionary.items():
        if v == value:
            s.append(k)
    for i in s:
        del a_dictionary[i]
    return a_dictionary
