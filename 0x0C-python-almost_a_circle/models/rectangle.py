#!/usr/bin/python3
"""Rectangle class inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of the rectangle"""

        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #"""

        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """print() & str() representation of Rectangle"""

        return f"[{type(self).__name__}] ({self.id})"\
               f" {self.x}/{self.y}"\
               f"- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        - 1st argument should be the id attribute
        - 2nd argument should be the width attribute
        - 3rd argument should be the height attribute
        - 4th argument should be the x attribute
        - 5th argument should be the y attribute"""

        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            else:
                self.__init__(self.width, self.height,\
                        self.x, self.y, self.id)

        elif kwargs:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
                else:
                    self.__init__(self.width,self.height,\
                            self.x, self.y, self.id)

    def to_dictionary(self):
        """returns the dictionary
        representation of a Rectangle"""

        my_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return my_dict
