#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixlistt = []

    for x in matrix:
        matrixlistt.append([y**2 for y in x])
    return matrixlistt