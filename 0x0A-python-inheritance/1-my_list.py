#!/usr/bin/python3
'''Python in Holberton'''


class MyList(list):
    '''Class inherited from list'''
    def print_sorted(self):
        '''prints the lists in ascending order'''
        print(sorted(self))
