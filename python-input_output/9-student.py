#!/usr/bin/python3
"""
This module defines a class Student
"""

class_to_json = __import__("8-class_to_json").class_to_json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
