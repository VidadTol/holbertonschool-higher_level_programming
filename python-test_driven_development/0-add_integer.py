#!/usr/bin/python3
"""
    This module provides a function to add two integers or floats
    a (int, float): First number, must be an integer or float.
    b (int, float): Second number, default is 98, must be an integer or float.
    Returns: int: The addition of a and b.
    Raises: TypeError: If a or b are not integers or floats.
    """


def add_integer(a, b=98):
    """
        Add to integers or floats
        a: first number b: second number

        The function accepts two numbers, whether they are integers or floats,
        converts them to integers if they are floats,
        and returns the sum of these two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return int(a + b)
