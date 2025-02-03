#!/usr/bin/python3
"""
Function that checks if an object is an instance
of a class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or an instance
    of a subclass of a_class
    """

    return isinstance(obj, a_class)
