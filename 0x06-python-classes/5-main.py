#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(-1)
my_square.my_print()

print("--")

my_square.size = 5
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
