#!/usr/bin/python3
'''Classes and objects project'''


class Rectangle:
    '''class Rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initializes the instance'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''Sets the way of depicting class info'''
        if self.__width == 0 or self.__height == 0:
            return ""
        string_r = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string_r += str(self.print_symbol)
            if i < (self.height - 1):
                string_r += '\n'
        return string_r

    def __repr__(self):
        '''Sets the way of depicting class info through repr'''
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        '''Set the way of deleting an instance'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Property to asign value to width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property to asign value to height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calculates rectangle's area'''
        return self.__width * self.__height

    def perimeter(self):
        '''calculates rectangle's perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the bigger rectangle accordin to area'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
