#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = (list(map(lambda rows: list(map(lambda columns: columns ** 2, rows)), matrix))) 
    return new
