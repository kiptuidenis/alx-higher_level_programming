#!/usr/bin/python3

class Robot:
    """Represents a robot with a name"""

    population = 0

    def __init__(self, name):
        self.name = name
        print("Robot {} is initialized.".format(self.name))

        Robot.population += 1

    def destroy(self):
        print("Robot {} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last Robot".format(self.name))
        else:
            print("There are still {} robots working.".format(Robot.population))

    def greet(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def count_robots(cls):
        print("We have {} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.greet()
Robot.count_robots()

droid2 = Robot("CPC-100")
droid2.greet()
Robot.count_robots()

print("Robots are working")

print("Robots have finished their work. So lets destroy them")
droid1.destroy()
droid2.destroy()

Robot.count_robots()
