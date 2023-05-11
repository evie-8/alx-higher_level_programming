#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import exit, argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+" or op == "-" or op == "*" or op == "/":
        if op == "+":
            print("{0:d} + {1:d} = {c:d}".format(a, b, c=add(a, b)))
        elif op == "-":
            print("{0:d} - {1:d} = {c:d}".format(a, b, c=sub(a, b)))
        elif op == "*":
            print("{0:d} * {1:d} = {c:d}".format(a, b, c=mul(a, b)))
        elif op == "/":
            print("{0:d} / {1:d} = {c:d}".format(a, b, c=div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
