#!/usr/bin/python3

import sys


def print_args():
    argv = sys.argv
    num_of_args = len(argv) - 1

    if (num_of_args == 0):
        print("{} arguments.".format(num_of_args))
        return
    if (num_of_args == 1):
        print("{} argument:".format(num_of_args))
        print("{}: {}".format(num_of_args, argv[num_of_args]))
        return
    print("{} arguments:".format(num_of_args))

    for args in range(1, num_of_args + 1):
        print("{}: {}".format(args, argv[args]))
    return


if __name__ == "__main__":
    print_args()
