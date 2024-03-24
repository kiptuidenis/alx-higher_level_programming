#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string"""
    new_str = list(my_string)
    print(new_str)
    new_str = [char for char in new_str if char != 'C' if char != 'c']
    new_str = ''.join(new_str)
    return new_str
