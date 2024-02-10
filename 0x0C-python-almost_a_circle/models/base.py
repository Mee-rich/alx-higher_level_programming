#!/usr/bin/python3
"""Module contains the class Base"""
import json
import os.path
import csv
import turtle

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries (list): list of dioctionaries.

        Returns:
            str: json string representation.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 
            list_objs to a file.

        Args:
            cls (type): class type (presumably inheriting from Base)
            list_objs (list): instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        
        Args: 
            json_string (str): string representing a
            list of dictionaries.
        
        Return:
            list: JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))


    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            cls: The class to save the attributes to
            **dictionary (list): A double pointer to a dictionary
        Returns:
            A dummy instance of Rectangle or Square
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        return (dummy)
