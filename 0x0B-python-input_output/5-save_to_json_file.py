#!/usr/bin/python3
"""save_to_json_file function definition"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file
    using a JSON representation"""
    
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
