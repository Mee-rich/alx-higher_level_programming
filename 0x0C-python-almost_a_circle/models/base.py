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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of rectangle or square in CSV

        Args:
            cls: the class
            list_objs (list): objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
            elif cls.__name__ == "Square":
                for i in list_objs:
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of rectangle or square in CSV.

        Args:
            cls: the class
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    dictionary = {"id": int(elm[0]), 
                                "width": int(elm[1]),
                                "height": int(elm[2]), 
                                "x": int(elm[3]), 
                                "y": int(elm[4])}

                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except Exception as e:
            print(f"Error: {e}")
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all th Rectangles and Squares.

        Args:
            list_rectangles (list): A list of rectangle objects to draw
            list_squares (list): A list of square objects to draw
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b731c")
        tur.pensize(3)

        tur.color("#ffffff")
        for rect in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rect.x, rect.y)
            tur.down()
            for i in range(2):
                tur.forward(rect.width)
                tur.left(90)
                tur.forward(rect.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b5e3d8")
        for sq in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sq.width)
            tur.up()
            tur.goto(sq.x, sq.y)
            tur.down()
            for i in range(2):
                tur.forward(sq.width)
                tur.left(90)
                tur.forward(sq.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
