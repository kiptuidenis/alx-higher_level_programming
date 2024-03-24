#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list
    (only once for each integer)"""
    uniq_list = set(my_list)
    uniq_list = list(uniq_list)
    sum = 0

    for int in range(len(uniq_list)):
        sum = sum + uniq_list[int]
    return sum
