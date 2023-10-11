#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    num = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for letter in roman_string:
        for key, value in romans.items():
            if letter == key:
                num = num + value
                break
    return num
