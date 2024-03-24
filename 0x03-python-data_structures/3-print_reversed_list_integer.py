#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse"""
    my_list.reverse()

    for integer in my_list:
        print("{:d}".format(integer))
    my_list.reverse()