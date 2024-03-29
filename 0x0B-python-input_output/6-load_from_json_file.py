#!/usr/bin/python3
"""Contains function taht creates a python obj from JSON file"""

def load_from_json_file(filename):
    """Creates a python obj from JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
