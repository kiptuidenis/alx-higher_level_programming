#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv

    length = len(argv)

    if length == 1:
        print("{} arguments.".format(0))
        exit()

    elif length == 2:
        print("{} argument:".format(length - 1))
    else:
         print("{} arguments:".format(length - 1))

    for args in range(1, length):
         print("{}: {} ".format(args, argv[args]))
