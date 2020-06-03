#!/usr/bin/python3
'''Python in Holberton'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class of a square inherited from Rectangle class'''
    def __init__(self, size):
        '''Instantiates square based on rectangle and adding size'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
