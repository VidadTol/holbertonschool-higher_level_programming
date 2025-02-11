#!/usr/bin/python3
"""
This module defines a function from_json_string
that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        The object represented by the JSON string.
    """
    return json.loads(my_str)
