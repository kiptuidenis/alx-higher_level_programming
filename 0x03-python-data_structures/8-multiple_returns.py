#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string
    and its first character"""
    if not sentence:
        return (1, None)
    length = len(sentence)
    char = sentence[0]

    return (length, char)