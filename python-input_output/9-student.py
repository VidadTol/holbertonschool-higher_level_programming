#!/usr/bin/python3
"""
This module defines a class Student
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
