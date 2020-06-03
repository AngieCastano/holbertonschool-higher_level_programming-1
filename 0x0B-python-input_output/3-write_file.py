#!/usr/bin/python3
'''I/O Python'''


def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8)
    and returns the number of characters written'''
    with open(filename, encoding='UTF-8', mode='w') as f:
        return f.write(text)
