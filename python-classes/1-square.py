#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    Private instance attribute: size Instantiation with size
    (no type/value verification)
    You are not allowed to import any module same thing as before
The Square class includes a private instance attribute size without type
or value checking at instantiation. It is initialized with an optional
size parameter via __init__(self, size)
    """
    def __init__(self, size):
        self.__size = size
