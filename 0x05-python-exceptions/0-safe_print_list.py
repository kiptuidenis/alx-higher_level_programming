#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Safely prints the contents of a list"""
    try:
        if x < 0:
            return 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print()
        return i + 1

    except (IndexError):
        print()
        return i
