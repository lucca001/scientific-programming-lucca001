"""
This function
"""

__author__ = "Michael Luccas & Cheo Reyes"

import numpy as np


def lowest_eigenvector(square_matrix, number_of_eigenvectors=3):

    import numpy as np

    m, n = square_matrix.shape

    if m != n:
        raise IndexError("Matrix is not square!")

    values, vectors = np.linalg.eig(square_matrix)
    values_sorted = np.sort(values)
    vectors_sorted = vectors[:, values.argsort()]

    return values_sorted[:number_of_eigenvectors+1], vectors_sorted[:number_of_eigenvectors+1]
