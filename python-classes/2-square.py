#!/usr/bin/python3

class Square:
    """
    This module defines a class Square that represents a square.
"""

    def __init__(self, size=0):
        """"
        Initializes a new Square instance.

        Parameters
        ----------
        size : int, optional
            The size of one side of the square (default is 0).
            Must be an integer and greater than or equal to 0.

        Raises
        ------
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
