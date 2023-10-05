#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv


def calculator():
    length = len(argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))

    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))

    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))

    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    return


if __name__ == "__main__":
    calculator()
