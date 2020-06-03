#!/usr/bin/python3
'''I/O Python'''


def number_of_lines(filename=""):
    '''returns the number of lines of a text file'''
    with open(filename, encoding='UTF-8') as f:
        return len(f.readlines())
