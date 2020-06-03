#!/usr/bin/python3
'''Python in Holberton'''


class MyInt(int):
    '''Class inherited from int'''
    def __eq__(self, oposite):
        '''Refers to equal to'''
        return False

    def __ne__(self, other):
        '''Refers to not equal to'''
        return True
