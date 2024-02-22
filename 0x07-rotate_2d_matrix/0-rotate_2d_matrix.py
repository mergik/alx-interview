#!/usr/bin/python3
"""rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """rotate an n x n 2D matrix by 90 degrees clockwise"""
    new = matrix[::-1]
    result = []
    tups = list(zip(*new))
    for tup in tups:
        result.append(list(tup))
    matrix[:] = result
