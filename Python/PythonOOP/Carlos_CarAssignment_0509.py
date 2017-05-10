#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Car
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price,
speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create six different instances of the class Car. In the class have a method called display_all() that returns all
the information about the car as a string. In your __init__(), call this display_all() method to display information
about the car once the attributes have been defined.

A sample output would be like this:

Price: 2000
Speed: 35mph
Fuel: Full
Mileage: 15mpg
Tax: 0.12
Price: 2000
Speed: 5mph
Fuel: Not Full
Mileage: 105mpg
Tax: 0.12
Price: 2000
Speed: 15mph
Fuel: Kind of Full
Mileage: 95mpg
Tax: 0.12
Price: 2000
Speed: 25mph
Fuel: Full
Mileage: 25mpg
Tax: 0.12
Price: 2000
Speed: 45mph
Fuel: Empty
Mileage: 25mpg
Tax: 0.12
Price: 20000000
Speed: 35mph
Fuel: Empty
Mileage: 15mpg
Tax: 0.15
"""


class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print("Your car price is: {0}.\nIt has a speed of: {1}.\nIts fuel is: {2}.\nIts mileage is: {3}.\nTax: {4}"
              .format(self.price, self.speed, self.fuel, self.mileage, self.tax))
        return self


first_car = Car(200, "10mph", "1/4 tank", "4mpg")
second_car = Car(50000, "200mph", "Full", "15mpg")
third_car = Car(9999, "80mph", "half tank", "40mpg")
fourth_car = Car(7499, "50mph", "Full", "100mpg")
fifth_car = Car(1000000, "250mph", "Emtpy", "0.5mpg")
sixth_car = Car(1500, "65mph", "Full", "30mpg")

newlist = [first_car, second_car, third_car, fourth_car, fifth_car, sixth_car]
for items in newlist:
    items.display_all()
