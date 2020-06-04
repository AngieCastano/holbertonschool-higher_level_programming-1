#!/usr/bin/python3
'''I/O Python'''


class Student():
    '''Simple class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def list_of_str(self, my_list):
        if type(my_list) is not list:
            return False
        for item in my_list:
            if type(item) is not str:
                return False
        return True

    def to_json(self, attrs=None):
        '''returns the dictionary description'''
        if self.list_of_str(attrs):
            return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}
        else:
            return self.__dict__
