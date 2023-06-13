#!/usr/bin/python3
"""writing to files"""


def write_file(filename="", text=""):
    """write to file or over write"""
    with open(filename, mode="w", encoding="utf-8") as f:
        length_char = f.write(text)
    return length_char
