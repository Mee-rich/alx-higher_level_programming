#!/usr/bin/python3
"""MyList module"""

class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """prints a sorted copy of the list"""
        print(sorted(self))
