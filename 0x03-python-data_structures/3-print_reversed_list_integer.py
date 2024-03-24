#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse"""
    if not my_list:
        return
    for int in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[int]))