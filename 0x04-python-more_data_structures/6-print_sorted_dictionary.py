#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.keys())
    for k in a:
        print(f"{k}: {a_dictionary[k]}")
