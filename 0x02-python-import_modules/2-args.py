#!/usr/bin/python3

from sys import argv

def printArgs():
    length = len(argv)

    if length == 1:
        print("0 arguments.")
        return

    elif length == 2:
        print("{} argument:".format(length - 1))
    else:
         print("{} arguments:".format(length - 1))

    for args in range(1, length):
         print("{}: {} ".format(args, argv[args]))

    return

if __name__ == "__main__":
    printArgs()
