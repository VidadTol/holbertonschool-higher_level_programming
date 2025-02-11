#!/usr/bin/python3
"""
This module defines a class Student with a method to_json
that retrieves a dictionary representation of a Student instance
"""


class Student:
    """
    A class representing a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to include in the
            dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict
