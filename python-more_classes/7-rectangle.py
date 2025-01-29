#!/usr/bin/python3
"""
    Module that defines a class Rectangle
    """


class Rectangle:
    """
    This code creates a Rectangle class that defines a rectangle
    with private instance attributes for width and height, validating
    them via properties and setters. The class should include public
    class attributes: number_of_instances (initialized to 0 and modified
    when objects are instantiated and deleted) and print_symbol
    (initialized to # and used for string representation). The class should
    also include public methods to calculate the area and perimeter, display a
    visual representation of the rectangle with the symbol print_symbol,
    and provide a __repr__ method to return a string to recreate the instance.
    A "Bye rectangle..." message should be printed when an instance is deleted.
    """
    number_of_instances = 0
    print_of_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        symbol = str(getattr(self, "print_symbol", Rectangle.print_of_symbol))
        return "\n".join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
