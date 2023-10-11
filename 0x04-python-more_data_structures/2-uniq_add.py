#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""

    new_set = set(my_list)
    new_list = list(new_set)
    sum = 0
    for integer in new_list:
        sum = sum + integer

    return sum
