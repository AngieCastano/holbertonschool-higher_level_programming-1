#!/usr/bin/python3
'''I/O Python'''


def read_lines(filename="", nb_lines=0):
    '''reads n lines of a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding='UTF-8') as f:
        read_lines = 0
        num_lines = len(f.readlines())
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= num_lines:
            print(f.read(), end='')
        else:
            while read_lines < nb_lines:
                print(f.readline(), end='')
                read_lines += 1
