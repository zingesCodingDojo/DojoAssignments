#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2


# dir(urllib2)
# help(urllib2)

"""
class User
By now, you should have a better understanding of the user class we showed you at the beginning of this chapter!

So far we've learned how to do a handful of things:

Define new classes
Add attributes that describe the state of our objects
Add methods that describe the behavior of our objects
initialize our instances with the __init__() method
naming and passing default parameters
Import and create new modules that we can use in our files/classes
Here is our User class with some comments to help you review:

# instantiate class User
class User(object):
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes from
        self.name = name
        self.email = email
        self.logged = True
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    # print name and email of the calling instance
    def show(self):
        print "My name is {}, and I am a {}. You can email me at {}".format(self.name, self.permission, self.email)
        return self
"""

class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.miles += miles
        return self
    def reverse(self,miles):
        self.mile -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

#class Parent(object): # inherits from the object class
  # parent methods and attributes here
#class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes

def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three", "four", "five") # output: "Got one and two, three"