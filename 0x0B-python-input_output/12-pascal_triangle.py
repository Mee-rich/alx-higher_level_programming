#!/usr/bin/python3
"""contains the pascal_triangle function"""

def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    
    return triangle
