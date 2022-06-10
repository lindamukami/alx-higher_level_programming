#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixlist = []

    for x in matrix:
        matrixlist.append([y**2 for y in x])
    return matrixlist
