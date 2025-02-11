#!/usr/bin/python3

"""
This module defines a function read_file that
reads a text file and prints its content.
"""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
