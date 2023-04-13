#!/usr/bin/python3
"""A Student class"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Student initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance:
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved
        Otherwise, all attributes must be retrieved"""

        if type(attrs) == list\
                and all(type(element) == str for element in attrs):
            attrs_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attrs_dict[attr] = getattr(self, attr)
            return attrs_dict

        return self.__dict__
