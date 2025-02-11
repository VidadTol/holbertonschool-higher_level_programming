#!/usr/bin/python3
"""
This module defines a function to_json_string
that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
