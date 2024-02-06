#!/usr/bin/python3
"""Module contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that returns dictionary representation
of requested attributes or all if none were requested
"""

class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        for json serialization
        
        Return:
            only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.key():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attributs of json to self
        """
        for key, value in json.items():
            setattr(self, key, value)
