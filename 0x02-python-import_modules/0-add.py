#!/usr/bin/python3

from add_0 import add


def add_nums():
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))

    return

if __name__ == "__main__":
    add_nums()