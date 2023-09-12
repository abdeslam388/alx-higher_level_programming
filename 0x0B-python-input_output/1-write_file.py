#!/usr/bin/python3
"""
Module to write a string to a text file and
return the number of characters written.
"""


def write_file(filename="", text=""):
    """ Write the specified text to the specified text file and
    return the number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)

