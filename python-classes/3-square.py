#!/usr/bin/python3

class Square:
    """
    This is a class named Square with a private instance attribute
    """

    def __init__(self, size=0):
        """
        The constructor of the Square class

        Args:
            size (int): The size of the square

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
        return self.__size ** 2
