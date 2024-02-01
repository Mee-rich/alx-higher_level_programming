#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting of
    the multiplication of m_a and m_b."""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floatsm_a should contain only integers or floats")
   
    for row in m_b:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floatsm_a should contain only integers or floats")
    
        def check_matrix_validity(matrix, matrix_name):
            row_lengths = [len(row) for row in matrix]
            if not all(elem == row_lengths[0] for elem in row_lengths):
                raise TypeError(f"Each row of {matrix_name} must be of the same size")
    
    check_matrix_validity(m_a, "m_a")
    check_matrix_validity(m_b, "m_b")

    row_len = []
    for row in m_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_a must be of the same size")

    a_rows, a_cols = len(m_a), len(m_a[0])
    b_rows, b_cols = len(m_b), len(m_b[0])
    
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(b_cols)] for _ in range (a_rows)]

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
