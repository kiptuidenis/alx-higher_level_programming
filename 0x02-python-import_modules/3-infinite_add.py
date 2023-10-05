#!/usr/bin/python3

import sys


def add_all_args():
    argv = sys.argv
    argv_len = len(argv)
    sum = 0

    for args in range(1, argv_len):
        sum = sum + int(argv[args])

    print(sum)


if __name__ == "__main__":
    add_all_args()
