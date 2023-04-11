#!/usr/bin/python3
"""Different Geometry module definition"""


class BaseGeometry:
    """BaseGeometry definition"""

    def area(self):
        """Raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle definition"""

    def __init__(self, width, height):
        """Rectangle initialization"""

        self.__width = width
        self.__height = height

        if self.__width:
            BaseGeometry.integer_validator(self, "width", self.__width)
        if self.__height:
            BaseGeometry.integer_validator(self, "height", self.__height)
