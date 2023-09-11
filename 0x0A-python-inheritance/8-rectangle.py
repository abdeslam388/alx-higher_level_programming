#!/usr/bin/python3
"""Inheris from baseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the documentation for the Rectangle class.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

