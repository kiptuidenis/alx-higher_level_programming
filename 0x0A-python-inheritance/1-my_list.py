#!/usr/bin/python3
"""Contains a class that inherits from list"""


class MyList(list):
    """Prints the list in a sorted manner
    """
    def __init__(self, *args):
        """Initialises the list"""
        super().__init__(*args)

    def print_sorted(self):
        """Prints sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
