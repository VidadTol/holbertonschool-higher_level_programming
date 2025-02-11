#!/usr/bin/python3

"""
This module defines a function read_file that
reads a text file and prints its content.
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
