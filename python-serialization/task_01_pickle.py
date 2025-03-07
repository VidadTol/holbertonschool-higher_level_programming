#!/usr/bin/env python3
"""
This module defines a class CustomObject and demonstrates
basic serialization using pickle.

"""


import pickle


class CustomObject:
    """
    A class representing a custom object.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject instance.
        """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the CustomObject instance to a file.

        Args:
            filename (str): The name of the file to save
            the serialized object to.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to load
            the serialized object from.

        Returns:
            CustomObject: The deserialized CustomObject instance.
        """
        try:

            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("File not found")
            return None
        except EOFError:
            print("Reached end of file")
            return None
