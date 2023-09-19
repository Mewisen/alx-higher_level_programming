#!/usr/bin/python3
"""
<<<<<<< HEAD

Module composed by a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

=======
Module composed by a function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """ Function that multiples 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
<<<<<<< HEAD
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


=======
        TypeError: if rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
<<<<<<< HEAD

=======
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")

    for elems in m_b:
        if not isinstance(elems, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
<<<<<<< HEAD

=======
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not type(elems) in (int, float):
<<<<<<< HEAD
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

=======
                raise ValueError("m_a should contain only integers or floats")
    for lists in m_b:
        for elems in lists:
            if not type(elems) in (int, float):
                raise ValueError("m_b should contain only integers or floats")
    length = 0
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    for elems in m_a:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elems)

    length = 0
<<<<<<< HEAD

=======
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    for elems in m_b:
        if length != 0 and length != len(elems):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elems)

    if len(m_a[0]) != len(m_b):
<<<<<<< HEAD
        raise ValueError("m_a and m_b can't be multiplied")
=======
            raise ValueError("m_a and m_b can't be multiplied")
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7

    r1 = []
    i1 = 0

    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
<<<<<<< HEAD
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
=======
        while (i1 < len(m_b[0])):
            num = a[i1] * m_b[i1][i2]
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1
