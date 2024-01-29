#!/usr/bin/python3
""" This module defines a rectangle"""

class Rectangle:
    """ A rectangle based on 0-rectangle module"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle
        Args:
            width: width
            height: height
        Raises: 
            TypeError: If size is not integer
            ValueError: If size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ field width is private"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter method to change width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0 :
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """field height is private"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to change height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """The public area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """The public perimeter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return (0)
        else:
            return ((2*self.__width) + (2*self.__height))
