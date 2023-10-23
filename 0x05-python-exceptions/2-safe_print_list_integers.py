#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Safely prints the contents of a list"""
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1

        except (ValueError, TypeError):
            i = i + 1

    print("")
    return ret
