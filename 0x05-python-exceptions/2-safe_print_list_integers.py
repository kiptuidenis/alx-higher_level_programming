#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements of a list and only integers."""
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return i + 1
    except (ValueError, IndexError):
        print()
        return i
