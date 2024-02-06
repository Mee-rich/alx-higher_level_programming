#!/usr/bin/python3
"""Module containing the append_write function"""

def append_write(filename="", text=""):
    """appends to text file and returns the num of chars added"""
    
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
