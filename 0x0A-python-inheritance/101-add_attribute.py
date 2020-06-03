#!/usr/bin/python3
'''Python in Holberton'''


def add_attribute(obj, attribute, value):
    '''adds a new attribute to an object if it’s possible'''
    if not obj.__class__.__module__ == 'builtins':
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
