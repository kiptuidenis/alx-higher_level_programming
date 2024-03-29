#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    item_a_0, item_a_1, *other = tuple_a + (0, 0)[:2 - len(tuple_a)]
    item_b_0, item_b_1, *other = tuple_b + (0, 0)[:2 - len(tuple_b)]

    first_elem = item_a_0 + item_b_0
    second_elem = item_a_1 + item_b_1
    tuple_sum = (first_elem, second_elem)
    return tuple_sum
