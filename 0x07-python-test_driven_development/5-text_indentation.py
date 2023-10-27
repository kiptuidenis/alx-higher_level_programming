#!/usr/bin/python3
"""This module prints the given text
"""


def text_indentation(text):
    """This function prints the text based on the following conditions:
    text must be a string, otherwise raise a TypeError exception with
    the message text must be a string
    There should be no space at the beginning or at the end of each printed line

    Args: text
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    i = 0

    while(i < len(text)):
        if text[i] in ('.', '?', ':'):
            print(text[i])
            print()

            if i == len(text) - 1:
                break

            if text[i + 1] in (' '):
                i += 2
            else:
                i += 1
        else:
            print(text[i], end="")
            i += 1
