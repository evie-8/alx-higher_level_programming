#!/usr/bin/python3
def print_last_digit(number):
    rem = abs(number) % 10
    print("{}".format(rem), end="")
    return rem
