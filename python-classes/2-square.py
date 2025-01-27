#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size',
and includes methods for initialization and validating the size.
"""


class Square:
    """
    This is a class named Square with a private instance attribute

    attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        initializes the square with a size

        Args:
            size (int): The size of the square (default is 0)

        must be an integer that is 0 or greater

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
