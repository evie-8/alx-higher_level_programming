#!/usr/bin/python3
"""JSON object representation"""

import json


def from_json_string(my_obj):
    """json string representation to python"""
    return json.loads(my_obj)
