#!/usr/bin/python3
"""
    This module defines a class Square
    """


class Square:
    """
    The `Square` class includes a private instance attribute `size`.
    It is instantiated with an optional `size` parameter
    using `__init__(self, size=0)`. The `size` must be an integer
    (raises `TypeError` if not) and ≥ 0 (raises `ValueError` if not).
    The class also has a public instance method `area` that returns
    the current square area.
"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
