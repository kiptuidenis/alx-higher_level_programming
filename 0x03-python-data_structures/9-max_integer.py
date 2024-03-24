#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if not my_list:
        return None
    max = float('-inf')
    for integer in my_list:
        if integer > max:
            max = integer
    return max