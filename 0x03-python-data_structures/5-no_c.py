#!/usr/bin/python3


def no_c(my_string):
    new_list = [x for x in my_string if x != 'C' and x != 'c']
    new_string = ''.join(new_list)

    return new_string
