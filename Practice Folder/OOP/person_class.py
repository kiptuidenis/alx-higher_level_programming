#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi my name is {}".format(self.name))
        self.name = "John"
        print("You can also call me {}".format(self.name))
    def say_hi_again(self):
        print("Hi my name is {}".format(self.name))
        self.name = "Willy"
        print("You can also call me {}".format(self.name))

p1 = Person("Denis")
p1.say_hi()
p1.say_hi_again()
