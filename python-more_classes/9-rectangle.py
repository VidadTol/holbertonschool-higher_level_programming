#!/usr/bin/python3
"""
    Module that defines a class Rectangle
    """


class Rectangle:
    """
    The Rectangle class defines a rectangle with private instance
    attributes for width and height, with properties and setters that
    validate these values. Width and height must be integers and cannot
    be negative. The class has public class attributes number_of_instances,
    which is initialized to 0 and updated when instances are instantiated
    and deleted, and print_symbol, initialized to # but can be any type.
    Instances are created with optional widths and heights.The class
    includes methods to calculate the area and perimeter, display the
    rectangle with print_symbol , and provide a __repr__ method to
    recreate an instance. A "Bye rectangle..." message is printed
    when an instance is deleted. The static method bigger_or_equal
    compares two rectangles based on their area and returns the larger
    one or rect_1 if they are equal. The square class method creates
    a new Rectangle instance with width and height equal to size
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
