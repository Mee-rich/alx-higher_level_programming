#!/usr/bin/python3

"""
This module is a function that prints a squarewith the character #
"""

def print_square(size):
    """
    Function that prints a square with the # character

    Args: 
        size: size of the square printed
    Raises:
        TypeError: If size is not an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print('#' * size)
