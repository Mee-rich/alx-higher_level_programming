#!/usr/bin/python3
"""Module containing is_same_class_method"""

def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified  class
    False: otherwise
    """
    return isinstance(obj, a_class) and type(obj) is a_class
