#!/usr/bin/python3
"""Module to read and print the content of a text file."""


def read_file(filename=""):
    """Read the content of the specified text file and print it to stdout.

    Args:
        filename (str): The name of the text
        file to read (default: empty string).
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")

