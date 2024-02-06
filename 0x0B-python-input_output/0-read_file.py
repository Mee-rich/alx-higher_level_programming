#!/usr/bin/python3
""" This module contains the read_file function """

def read_file(filename=""):
    """Print the content of a UTF-8 textfile to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

