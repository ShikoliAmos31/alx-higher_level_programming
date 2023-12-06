#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]

    return new_matrix


# Test the function with the provided example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
