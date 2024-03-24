#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position"""
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list

    my_list[idx] = element
    return my_list
