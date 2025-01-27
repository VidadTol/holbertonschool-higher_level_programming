#!/usr/bin/python3
"""
    this module defines a class named Square with a private
    instance attribute size
    and a public instance method area that returns the area of the square
    """


class Square:
    """
    a class that defines a square by the size of one
    of its sides includes a method to compute
    the area of the square.

    Attributes:
        size (int): The size of the square
"""

    def __init__(self, size=0):
        """
        initialize a new square instance

        Args:
            size (int): The size of the square (default = 0)
            must be an integer that is 0 or greater

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        calculates and returns the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
