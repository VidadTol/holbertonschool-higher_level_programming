#!/usr/bin/python3
"""
This module defines a function load_from_json_file that
creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
