#!/usr/bin/python3
"""Module to append a string to the end of a
text file and return the number of characters added."""


def append_write(filename="", text=""):
    """Append the specified text to the specified
    text file and return the number of characters added.

    Args:
        filename (str): The name of the text
        file to append to (default: empty string).
        text (str): The text to append to the file (default: empty string).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

