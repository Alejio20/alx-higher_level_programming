#!/usr/bin/python3
"""A Retangle class definition"""


class Rectangle():
    """A Rectangle class representation"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
                Arguments:
                    width: represents the width of the rectangle
                    height: represents the height of the rectangle
                Error Raises:
                    TypeError: if size is not integer
                    ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Diagram representation of the rectangle using #"""
        rectangle_diag = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_diag
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle_diag += "#"
            if column < (self.__height - 1):
                rectangle_diag += "\n"
        return rectangle_diag

    def __repr__(self):
        """String representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
