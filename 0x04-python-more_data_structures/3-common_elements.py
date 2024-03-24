#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets"""
    comm_set = {x for x in set_1 if x in set_2}
    return comm_set