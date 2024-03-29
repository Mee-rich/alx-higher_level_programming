#!/usr/bin/python3

"""
This module is made of functions that divides the numbers of a matrix
"""

def matrix_divided(matrix, div):
    """
    Function that divided the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number that divides the matrix
    Returns:
        A new matrix
    Raises:
        TypeError: 
                If the elements of the matrix aren't lists
                If the lists of the matrix don't have the same size
                If the elements of the lists aren't integers/floats
                If div is not an integer/float number
        ZeroDivisionError: If div is zero
    """
    
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = 0

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if length != 0 and len(elements) != length:
            raise TypeError("Each row of the matrix must have the same size")

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
         
        length = len(elements)

        result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
        
        return (result)
                    
