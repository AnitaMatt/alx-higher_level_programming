#!/usr/bin/python3
"""Function that divides all elements of a matrix"""
def matrix_divided(matrix, div):
    """ checking that the matrix is a list of list and other errors"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for ele in row:
            if not isinstance(ele, (int,float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if not all(len(i) == len(matrix[0])  for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_m = []
    for i in matrix:
        new_m.append(list(map(lambda el: round(el / div, 2), i)))
    return new_m
