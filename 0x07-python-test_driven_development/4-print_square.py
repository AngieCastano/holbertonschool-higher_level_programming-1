#!/usr/bin/python3
'''prints a square with the character #, with len of <size>'''


def print_square(size):

    '''prints a square with the character #, with len of <size>'''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
