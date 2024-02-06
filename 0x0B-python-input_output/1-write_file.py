#!/usr/bin/python3
"""Module containing the write-file function"""

def write_file(filename="", text""):
    """Writes to text file and returns num chars written"""

    with open(filename, mode="w",  encoding="utf-8") as f:
        return (f.write(text))
