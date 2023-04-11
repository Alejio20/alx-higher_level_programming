#!/usr/bin/python3
"""Rectangle inherits BaseGeometry"""
BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle definition"""

    def __init__(self, width, height):
        """Rectangle initialization"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)
