#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after each matching line.
    """
    lines = []

    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(lines)

