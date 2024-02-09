#!/usr/bin/python3
"""Defines a class that inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """Class that defines the properties of Rectangle.

    Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0).
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
       """Prints rectangle"""
       return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height))
    
    @property
    def width(self):
        """Width retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        
        Args:
            value (int): width of rectangle.

        Raises:
            TypeError: if width is not an integer.
            valueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property 
    def height(self):
        """Height retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value(int): height of rectangle.
        
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x retriever.

        Returns:
            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """property setter for x.

        Args:
            value (int): x.

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is less than zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retriever for y.

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """property setter for y.

        Args:
            value (int): x.

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of a rectangle.

        Returns:
            int: area.
        """
        return (self.__width * self.height)

    def display(self):
        """Prints in stdout the Rectangle 
            instance with the character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        
        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        #print("args {}".format(type(args)))
        #print("kwargs (dict): double pointer to a dictionary
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle

        """
        return {'id': getattr(self, "id"), 'width': getattr(self, "width"),
                'height': getattr(self, "height"), 'x': getattr(self, "x"),
                'y': getattr(self, "y")}


