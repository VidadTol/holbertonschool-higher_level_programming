#!/usr/bin/python3
"""
This module defines a class Student with methods to_json
and reload_from_json that retrieve a dictionary representation
of a Student instance and update the instance attributes
from a JSON object, respectively
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
