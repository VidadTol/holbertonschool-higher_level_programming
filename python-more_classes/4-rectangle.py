#!/usr/bin/python3
"""
    Module that defines a class Rectangle
    """


class Rectangle:
    """
    A Rectangle class that defines a rectangle with private instance
    attributes for width and height, validating them via properties
    and setters.The class should include public methods to calculate
    the area and perimeter of the rectangle. Additionally,
    the __str__ method should provide a visual representation of
    the rectangle using the # character, with special handling
    for zero dimensions. Finally, the __repr__ method should
    return a string representation of the rectangle that would
    theoretically allow recreating an instance with the same dimensions.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width},{self.height})"
