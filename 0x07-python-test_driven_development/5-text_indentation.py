#!/usr/bin/python3

"""
Module composed of a function that prints 2 new lines after ".?:" characters
"""

def text_indentation(text):
    """ Function that prints a new line after ".?:" characters
    Args:
        text: input string
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(line.strip(" ") for line in text.split(delim))

    print(text, end="")
