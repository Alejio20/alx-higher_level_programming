#!/usr/bin/python3
"""
Module definition for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given number

    Raise:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0

    Arguments:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)

    Return: A new matrix which represents the result of the divisions
    """

    if matrix is [[]]: # check if matrix is a list of lists
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if matrix: # check for the length of first list in the matrix
        matrix_len = len(matrix[0])

    if not (isinstance(div, int) or isinstance(div, float)): # div must be integer or float
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [] # create a new list
    for i in range(len(matrix)):
        if len(matrix[i]) != matrix_len: # Check for equal size of lists in  matrix
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([]) # make a list of list
        for j in matrix[i]:
            if type(j) is int or type(j) is float: # check that matrix element is a number
                new_matrix[i].append(round((j / div), 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return (new_matrix)
