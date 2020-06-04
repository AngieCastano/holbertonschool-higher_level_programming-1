#!/usr/bin/python3
'''I/O Python'''


class Student():
    '''Simple class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns the dictionary description'''
        if attrs is None or attrs == []:
            return self.__dict__
        else:
            return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}
