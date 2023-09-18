#!/usr/bin/python3
""" Base module """

import json
import csv
import turtle


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**dict_obj) for dict_obj in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            new_instance = cls(1)  # Create a dummy instance
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("")
            else:
                writer = csv.writer(file)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        data = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                objects = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    objects.append(obj)
                return objects
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Initialize Turtle graphics
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Shapes Drawing")

        # Create a Turtle object
        pen = turtle.Turtle()
        pen.speed(1)

        # Draw rectangles from the list
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.end_fill()

        # Draw squares from the list
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        # Close the Turtle graphics window when clicked
        screen.exitonclick()


if __name__ == "__main__":
    pass

