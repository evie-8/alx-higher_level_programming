#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = list(map(lambda i: list(map(lambda x: x ** 2, i)), matrix))
    return new
