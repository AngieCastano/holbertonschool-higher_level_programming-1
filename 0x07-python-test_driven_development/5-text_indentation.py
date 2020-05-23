#!/usr/bin/python3
'''prints a text with 2 new lines after each
    of these characters: ., ? and :'''


def text_indentation(text):
    '''prints a text with 2 new lines after each
    of these characters: ., ? and :'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    '''Switch turns to 1 when a '.' '?' or ':' has been printed
    to skip whitespaces'''
    switch = 0
    if text[0] == ' ':
        switch = 1
    for index in range(len(text)):
        if text[index] in ['.', '?', ':']:
            print(text[index], end="")
            print('\n')
            '''When a '.' '?' or ':' is found switch turns to 1'''
            switch = 1
        else:
            if switch == 0:
                print(text[index], end="")
            elif switch == 1 and text[index] == ' ':
                '''When switch is 1 we don't have to print  whitespaces'''
                continue
            else:
                print(text[index], end="")
                switch = 0
