#!/usr/bin/python3
'''Divides all elements of a matrix'''


def matrix_divided(matrix, div):
    ''' divides all elements of a matrix
    usage: matrix_divided(matrix, div)'''

    # Validations for data

    # Div validations

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Matrix validations
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    len_item = len(matrix[0])
    for row in matrix:
        if len(row) != len_item:
            raise TypeError("Each row of the matrix must have the same size")

    # Execution of division
    new = [[round(row[i]/div, 2) for i in range(
        len(matrix[1]))] for row in matrix]
    return new_matrix
