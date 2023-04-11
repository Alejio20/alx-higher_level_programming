#!/usr/bin/python3
"""Square inherits Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """Square definition"""
    
    def __init__(self, size):
        """Square initialization"""
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
