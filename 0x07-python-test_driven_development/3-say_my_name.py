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
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    
    if last_name is not None and not isinstance(last_name, str):
        raise TypeError("last anme must be a string")
   
    if last_name is not None:
        return (f"My name is {first_name} {last_name}")
    else:
        return (f"My name is {first_name}")
