#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    largest = 0
    larg_key = ''

    for key, value in a_dictionary.items():
        if value >= largest:
            largest = value
            larg_key = key
    return larg_key