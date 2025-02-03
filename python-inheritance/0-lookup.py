#!/usr/bin/python3
"""
The function should return the list of available attributes
and methods of an object:
    """


def lookup(obj):
    """
    This function uses the built-in dir() function to get the list
    of attributes and methods of the object passed as a parameter.
    """
    return dir(obj)
