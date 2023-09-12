#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None, retrieve all attributes. Default is None.

        Returns:
            dict: A dictionary containing
            the specified attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing
            attribute names as keys and their values.
        """
        for attr, value in json.items():
            setattr(self, attr, value)

