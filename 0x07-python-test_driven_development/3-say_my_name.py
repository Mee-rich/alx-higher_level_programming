#!/usr/bin/python3
"""
This module is composed by a function prints a message
"""

def say_my_name(first_name, last_name=""):
    """ Function taht prints "My name is <first name> <last name>"
    Args:
        first_name: first name
        last_name: last name

    Raises:
            TypeError: If name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first name must be string")

    if type(last_name) is not str:
        raise TypeError("last name must be string")

    print("My name is {} {}".format(first_name, last_name))
