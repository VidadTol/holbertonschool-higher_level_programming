#!/usr/bin/python3
"""
This module defines a function load_from_json_file that
creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
