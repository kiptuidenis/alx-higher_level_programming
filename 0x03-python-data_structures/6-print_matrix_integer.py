#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        if len(row) == 0:
            print("")
            return
        for column in range(len(row)):
            if column < len(row) - 1:
                print("{:d} ".format(row[column]), end='')
            else:
                print("{:d}".format(row[column]))
    return
