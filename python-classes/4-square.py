#!/usr/bin/python3
"""
    This module defines a class Square
    """


class Square:
    """
    The Square class includes a private instance attribute size with
    property methods to retrieve and set it. The size must be an integer
    (raises TypeError if not) and ≥ 0 (raises ValueError if not).
    The class is instantiated with an optional size parameter
    using __init__(self, size=0).
    It includes a public instance method area that returns the current
    square area.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
