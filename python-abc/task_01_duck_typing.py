#!/usr/bin/env python3
"""
Import the necessary components from the abc module
"""

from abc import ABC, abstractmethod
import math

"""
Define the Shape class, ensuring it inherits from ABC to mark it as abstract
"""


class Shape(ABC):
    """
    Abstract class Shape that requires subclasses to implement
    the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(self):
    """
    Print the area and perimeter of a shape.
    """
    print(f"Area: {self.area()}")
    print(f"Perimeter: {self.perimeter()}")
