#!/usr/bin/python3
"""write json representation to a file"""


import json


def load_from_json_file(filename):
    """creates python object  from json file"""
    with open(filename) as f:
        return json.load(f)
