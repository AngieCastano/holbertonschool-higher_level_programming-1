#!/usr/bin/python3
'''Python in Holberton'''


def add_attribute(obj, attribute, value):
    '''adds a new attribute to an object if it’s possible'''
    if obj.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
