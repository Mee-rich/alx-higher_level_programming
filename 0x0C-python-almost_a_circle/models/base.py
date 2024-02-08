#!/usr/bin/python3
"""Module contains the class Base"""


class Base:
    """This class will be the base of all 
    other classes in this project
    
    Attributes:
            __nb_objects
  
    """
    __nb_objects = 0
   

    def __init__(self, id=None):
        """Initializes a new instance of Base

        Args:
            id (int, optional): Identity of each instance.
            Default to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
