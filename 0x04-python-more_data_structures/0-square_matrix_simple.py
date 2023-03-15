#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for m in matrix:
        new_matrix1 = []
        for n in m:
            new_matrix1.append(n ** 2)
        new_matrix.append(new_matrix1)
    return new_matrix
