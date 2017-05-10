#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Bike
Create a new class called Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph");
In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice,
reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?
"""


class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayinfo(self):
        print("This bike costs: {0}USD.\nIt has a max speed of: {1}.\nCurrently it has: {2} miles on it."
              .format(self.price, self.max_speed, self.miles))
        return self

    def ride(self):
        self.miles += 10
        print("Riding~~~~ now currently at: {0} miles ridden".format(self.miles))
        return self

    def reverse(self):
        self.miles -= 5
        print("Reversing~~~ decreasing miles ridden... now currently at: {0} miles ridden.".format(self.miles))
        return self

first_bike = Bike(100, "10mph")

# Ride three times and reverse once.
for x in xrange(3):
    first_bike.ride()
first_bike.displayinfo().reverse()

# Ride two times and reverse twice.
for y in xrange(2):
    first_bike.ride()
    first_bike.reverse()
first_bike.displayinfo()

# Reverse three times.
for n in xrange(3):
    first_bike.reverse()
first_bike.displayinfo()


# ALTERNATIVE METHOD
second_bike = Bike(100, "10mph")

# Tide three times and reverse once.
second_bike.ride().ride().ride().reverse().displayinfo()

# Ride two times and reverse twice.
second_bike.ride().ride().reverse().reverse().displayinfo()

# Reverse three times.
second_bike.reverse().reverse().reverse().displayinfo()
