#!/usr/bin/python3
'''Almost a circle project'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class inheriting from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiator'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Setting str representation'''
        return '[Rectangle] (' + str(self.id) + ') ' + str(self.x) + '/' + str(
            self.y) + ' - ' + str(self.width) + '/' + str(self.height)

    '''
    Getters
    '''

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    '''
    Setters
    '''

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    '''
    Public methods
    '''

    def area(self):
        '''
        returns the area value of the instance
        '''
        return self.width * self.height

    def display(self):
        '''
        Prints in stdout the Rectangle
        instance with the character #
        '''
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        returns the dictionary representation of
        a Rectangle instance
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        new_dict = {}
        for key in attrs:
            new_dict[key] = getattr(self, key)
        return new_dict

if __name__ == '__main__':
    Rectangle("1", 2)
