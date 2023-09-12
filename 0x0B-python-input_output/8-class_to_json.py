#!/usr/bin/python3
"""Module to return the dictionary description with
simple data structure for JSON serialization of an object."""


def class_to_json(obj):
    """Return the dictionary description with simple
    data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary description of the object for JSON serialization.
    """
    return obj.__dict__


if __name__ == "__main__":
    class MyClass:
        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

