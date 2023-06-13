#!/usr/bin/python3
"""reading files"""


def read_file(filename=""):
    """reading from file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
