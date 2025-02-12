#!/usr/bin/env python3
"""
This module defines functions for basic serialization
and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize data to JSON and save it to a file.

    Args:
        data: The data to serialize.
        filename (str): The name of the file to save the data to.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load data from a file and deserialize it from JSON.

    Args:
        filename (str): The name of the file to load the data from.

    Returns:
        The deserialized data.
    """
    

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
