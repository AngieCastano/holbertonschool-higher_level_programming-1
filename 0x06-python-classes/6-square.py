#!/usr/bin/python3
"""Defines Class square"""


class Square:

    """class Instantiation"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Property of  attribute size"""
    @property
    def size(self):
        return self.__size

    """Sets attribute size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Property of  attribute position"""
    @property
    def position(self):
        return self.__position

    """Sets attribute position"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple or value[0] < 0 or value[1] < 0 or len(value) != 2\
            or type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Public instance method- returns current area"""
    def area(self):
        return self.__size*self.__size

    """Public instance method- returns prints the square"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for cols in range(0, self.__position[1]):
                print("")
            for counter_total in range(0, self.__size):
                for counter_spaces in range(0, self.__position[0]):
                    print(" ", end="")
                for counter_row in range(0, self.__size):
                    print("#", end="")
                print("")
