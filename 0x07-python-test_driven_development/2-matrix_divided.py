<<<<<<< HEAD
#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


=======
 #!/usr/bin/python3
"""
This module composed by a function that divides the number of a matrix
"""

def matrix_divided(matrix, div):
    """ Fucntion that divides the integer/float numberof a matrix
    Args:
       matrix: list of a list of integers/floats
       div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the element of the matrix aren't lists
                   If the element of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
<<<<<<< HEAD

=======
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
<<<<<<< HEAD
            raise TypeError(msg_type)
=======
            raise TypeError(msg_size)
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
<<<<<<< HEAD
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
=======
                raise TypeError(msg_size)

        len_e = len(elems)
        m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
        return (m)
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
