#!/usr/bin/python3
"""this module defines a class
MyInt that inherits from int"""


class MyInt(int):
    """
    This is the documentation for the MyInt class.
    """

    def __init__(self, value):
        """
        Initialize the MyInt instance with a value.
        """
        super().__init__(value)

    def __eq__(self, other):
        """
        Define the == operator to be inverted.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Define the != operator to be inverted.
        """
        return super().__eq__(other)

