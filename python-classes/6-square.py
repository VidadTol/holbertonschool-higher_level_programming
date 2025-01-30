#!/usr/bin/python3
"""
    This module defines a class Square
"""


class Square:
    """
    The Square class includes private instance attributes size and position
    with property methods to retrieve and set them. The size must be an integer
    (raises TypeError if not) and ≥ 0 (raises ValueError if not). The position
    must be a tuple of 2 positive integers (raises TypeError if not). The class
    is instantiated with optional size and position
    It has a method area to return the square area and a method my_print to
    print the square using #, with correct
    positioning and handling when size is 0
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers ")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers ")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        # print empty lines based on the position
        for _ in range(self.__position[1]):
            print()
        # print the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
