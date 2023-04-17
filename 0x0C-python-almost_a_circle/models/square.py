#!/usr/bin/python3
"""Square class inherits from Rectangle class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class initialization"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print() & str() representation of Square"""

        return f"[{type(self).__name__}] ({self.id})" \
               f" {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        - 1st argument should be the id attribute
        - 2nd argument should be the size attribute
        - 3rd argument should be the x attribute
        - 4th argument should be the y attribute"""

        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                self.__init__(self.size, self.x, self.y, self.id)

        elif kwargs:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
                else:
                    self.__init__(self.size,\
                                  self.x, self.y, self.id)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        my_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

        return my_dict
