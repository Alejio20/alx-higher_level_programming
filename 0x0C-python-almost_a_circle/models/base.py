#!/usr/bin/python3
"""Base module for all other classes"""
import json
import csv
import turtle


class Base:
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the base class"""

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of list_dictionaries"""

        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs to a file"""

        with open(f"{cls.__name__}.json", mode="w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                my_list = []
                for obj in list_objs:
                    my_list.append(obj.to_dictionary())
                f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        try:
            with open(f"{cls.__name__}.json", mode="r") as f:
                json_dict = cls.from_json_string(f.read())
                return [cls.create(**dict) for dict in json_dict]
        except FileExistsError or FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs & save as CSV file"""

        with open(f"{cls.__name__}.csv", "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    field = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=field)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file & load data"""

        try:
            with open(f"{cls.__name__}.csv", "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    field = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=field)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileExistsError or FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#000000")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#00FF00")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#0000FF")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
