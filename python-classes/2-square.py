#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    The Square class includes a private instance attribute size.
    It is instantiated with an optional size parameter
    using __init__(self, size=0).
    The size must be an integer (raises TypeError if not) and ≥ 0
    (raises ValueError if not).
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
