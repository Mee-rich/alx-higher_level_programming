#!/usr/bin/python3
"""A class square that inherits from rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class defines properties of square.
    
    Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
        id (int): identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instance of the square.

        Args:
            size (int): width and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, oiptional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints a square representation"""

        return ("[{}] ({:d}) {:d}/{:d} - {:d}".format(type(self).__name__, self.id, self.x, self.y, self.size)) 

    @property
    def size(self):
        """property retriever for size.

        Returns:
            int: size of one side of square.

        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.

        Args:
            value (int): width of square
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """Updates the square and assign key/value argument to attributes.

        Args:
            *args - variable number of no-keyword
            **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            # If no positional arguments are provided, update using keyword arguments
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
