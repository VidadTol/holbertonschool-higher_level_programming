#!/usr/bin/python3

"""
    This module contains a function that prints a string with the first and last name.
"""

def say_my_name(first_name, last_name=""):

    """Prints a string with the first and last name.
    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.
    Returns:
        None: This function returns nothing.
    """ 

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
    