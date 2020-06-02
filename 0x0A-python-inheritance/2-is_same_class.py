#!/usr/bin/python3
def is_same_class(obj, a_class):
    if dir(obj) == dir(a_class):
        return True
    return False
