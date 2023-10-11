#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes square values of all integers"""
    if not matrix:
        return

    new_list = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return new_list
