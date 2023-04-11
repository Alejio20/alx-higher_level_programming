#!/usr/bin/python3
"""Rectangle inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle definition"""

    def __init__(self, width, height):
        """Rectangle initialization"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
