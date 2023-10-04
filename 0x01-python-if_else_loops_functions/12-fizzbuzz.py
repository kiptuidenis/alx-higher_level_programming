#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        mulOfThree = i % 3
        mulOfFive = i % 5

        if (mulOfThree == 0 and mulOfFive == 0):
            print("FizzBuzz", end=' ')
        elif (mulOfFive == 0):
            print("Buzz", end=' ')
        elif (mulOfThree == 0):
            print("Fizz", end=' ')
        else:
            print("{}".format(i), end=' ')
