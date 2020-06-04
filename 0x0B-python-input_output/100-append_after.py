#!/usr/bin/python3
'''I/O Python'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts <new_string> to <filename>,
    after each line containing <search_string>'''
    with open(filename, 'r') as f:
        buffer = list()
        for line in f:
            buffer.append(line)
            if search_string in line:
                buffer.append(new_string)

    with open(filename, 'w') as f:
        string = ''
        f.write(string.join(buffer))
