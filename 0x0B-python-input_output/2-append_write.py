#!/usr/bin/python3
"""writing to files"""


def append_write(filename="", text=""):
    """write to file or over write"""
    with open(filename, mode="a", encoding="utf-8") as f:
        length_char = f.write(text)
    return length_char
