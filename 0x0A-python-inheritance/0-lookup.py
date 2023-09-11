#!/usr/bin/python3
"""
    This modul returns a list of available
    attributes and imethods of an object.
"""


def lookup(obj):
    """A list of strings representing
    the attributes and methods of the object."""
    return dir(obj)
