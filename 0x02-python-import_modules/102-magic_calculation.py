#!/usr/bin/python3

import magic_calculation_102

def perform_calculation(a, b):
    if a < b:
        add = magic_calculation_102.add
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        sub = magic_calculation_102.sub
        return sub(a, b)
