#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""
    new_list = list(map(lambda row: list(map(lambda column: column ** 2, row)), matrix))
    return new_list
