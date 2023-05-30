#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for t in range(x):
        try:
            i = int(my_list[t])
        except (TypeError, ValueError):
            continue
        else:
            print("{:d}".format(i), end="")
            c += 1
    print()
    return c
