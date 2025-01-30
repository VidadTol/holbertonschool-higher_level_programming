#!/usr/bin/python3
"""
    Module that defines a class Rectangle
    """


class Rectangle:
    """
    This code creates a Rectangle class that defines a rectangle
    with private instance attributes for width and height, validating
    their assignment via properties and setters. The class should
    include public class attributes: number_of_instances
    (initialized to 0, incremented on instantiation, and decremented
    on deletion) and print_symbol (initialized to #, used for string
    representation,and can be of any type). The class should also include
    public methods to calculate the area and perimeter, display a visual
    representation of the rectangle with the symbol print_symbol,
    and provide a __repr__ method to return a string to recreate the instance.
    A "Bye rectangle..." message should be printed when an instance is deleted.
    Finally, a static method bigger_or_equal should compare two Rectangle
    instances based on their area and return the larger of the two,
    or rect_1 in case of equality.
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
