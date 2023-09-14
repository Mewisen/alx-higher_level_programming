<<<<<<< HEAD
#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


=======
#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    """

    return (np.matmul(m_a, m_b))
