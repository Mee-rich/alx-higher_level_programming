#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Input validation
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Input Validation: check if 'div' is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Input Validation: check if 'matrix' is a non-empty list of lists of integers/float
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be (list of lists) of integers/floats")

    row_length = 0 # Initialize a variable to keep track of the row length

    # Matrix size validation: ensure all rows have the same size
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError("matrix must be a natrix (list of lists) of integers/floats")

        if row_length != 0 and len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        # Element type validation: check that all elements in the matrix are numbers (int or float)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        row_length = len(row) #update the row length

        #Matrix Division
        result = [
                [round(element / div, 2) for element in row]
                for row in matrix
                ]
        return result 
