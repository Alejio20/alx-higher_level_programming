#!/usr/bin/python3
"""Defines a Square as a rectangle subclass"""
Rectantgle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """Square definition"""

    def __init__(self, size):
        """Square Initialization"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
