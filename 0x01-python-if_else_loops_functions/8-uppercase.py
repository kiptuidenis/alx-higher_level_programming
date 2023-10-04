#!/usr/bin/python3

def uppercase(str):
    for char in str:
        is_upper = ord(char)
        if (is_upper >= 97 and is_upper <= 122):
            char = chr(is_upper - 32)
        print("{}".format(char), end='')
    print("")
