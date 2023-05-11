#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{0:d} + {1:d} = {c:d}".format(a, b, c=add(a, b)))
    print("{0:d} - {1:d} = {c:d}".format(a, b, c=sub(a, b)))
    print("{0:d} * {1:d} = {c:d}".format(a, b, c=mul(a, b)))
    print("{0:d} / {1:d} = {c:d}".format(a, b, c=div(a, b)))
