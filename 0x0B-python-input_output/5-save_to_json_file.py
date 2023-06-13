#!/usr/bin/python3
"""write json representation to a file"""


import json


def save_to_json_file(my_obj, filename):
    """write json object representation to a file"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
