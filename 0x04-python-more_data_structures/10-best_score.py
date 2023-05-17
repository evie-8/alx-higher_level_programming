#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    a = max(a_dictionary.values())
    b = list(a_dictionary.values())
    c = list(a_dictionary.keys())
    return c[b.index(a)]
