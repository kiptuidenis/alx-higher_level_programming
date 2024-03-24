#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    print(myKeys)

    new_dict = {i: a_dictionary[i] for i in myKeys}
    for key, value in new_dict.items():
        print("{}: {}".format(key, value))