#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s = sum(x * y for x, y in my_list)
    t = sum(y for _, y in my_list)
    return s / t
