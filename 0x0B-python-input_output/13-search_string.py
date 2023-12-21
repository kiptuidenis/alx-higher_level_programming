#!/usr/bin/python3
"""This module finds a specific substring in a file"""
word = 'laptop'
with open('sales.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    print(lines)
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)