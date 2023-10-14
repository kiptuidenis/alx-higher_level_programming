#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    greater = 0
    smaller = 0
    roman_list = []
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman_string) == 1:
        if roman_string[0] not in romans:
            return 0
        for key, value in romans.items():
            if roman_string[0] == key:
                return value

    for letter in roman_string:
        if letter not in romans:
            return 0
        for key, value in romans.items():
            if letter == key:
                roman_list.append(value)
                break

    for i in range(0, len(roman_list)):
        j = i + 1
        if j == len(roman_list) - 1:
            if roman_list[i] > roman_list[j]:
                greater = greater + roman_list[i] + roman_list[j]
            if roman_list[i] < roman_list[j]:
                smaller = smaller + roman_list[i]
                greater = greater + roman_list[j]
            if roman_list[i] == roman_list[j]:
                if (roman_list[i] == 5 or roman_list[i] == 50
                or roman_list[i] == 500):
                    return 0
                greater = greater + roman_list[i] + roman_list[j]
            break

        else:
            if roman_list[i] > roman_list[j]:
                greater = greater + roman_list[i]
            elif roman_list[i] < roman_list[j]:
                smaller = smaller + roman_list[i]
            elif roman_list[i] == roman_list[j]:
                if (roman_list[i] == 5 or roman_list[i] == 50
                or roman_list[i] == 500):
                    return 0
                else:
                    greater = greater + roman_list[i]
    result = greater - smaller
    return result
