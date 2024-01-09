#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        numpy.ndarray: Resultant matrix.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    Examples:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        array([[ 7, 10],
               [15, 22]])

        >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        array([[13, 16]])
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("Incompatible matrices for multiplication")

if __name__ == "__main__":
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[
