#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if not roman_string:
        return 0

    prev_value = 0  # Initialize the previous value

    for letter in roman_string[::-1]:  # Reverse from right to left
        if letter not in romans:
            return 0
        value = romans[letter]
        if value < prev_value:
            result -= value  # Subtract the value if it's smaller than the prev
        else:
            result += value  # Add the value if it's greater or equal to
        prev_value = value  # Update the previous value for the next iteration

    return result
