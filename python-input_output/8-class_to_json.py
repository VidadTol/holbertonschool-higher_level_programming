#!/usr/bin/python3
"""
This module defines a function class_to_json that returns
the dictionary description with simple data structure
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """
    Return the dictionary description with simple data
    structure for JSON serialization of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
