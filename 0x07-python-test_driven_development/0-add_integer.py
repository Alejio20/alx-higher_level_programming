#!/usr/bin/python3
"""
This module has only the add_integer method
"""


def add_integer(a, b=98):
    """
    Returns an integer of the addition of a and b which can be int or float

    Arguments:
        a: first integer
        b: second integer with default value of 98

    Return:
        An integer addition of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
