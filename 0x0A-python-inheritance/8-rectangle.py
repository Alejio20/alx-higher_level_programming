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

        if width:
            self.integer_validator("width", width)
            self.__width = width
        if height:
            self.integer_validator("height", height)
            self.__height = height
