#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Making and Reading from Dictionaries
Create a dictionary containing some information about yourself. The keys should include name, age,
country of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
Copy
There are two steps to this process, building a dictionary and then gathering all the data from it.
Write a function that can take in and print out any dictionary keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs.
Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement
of any web application.
"""

# Creating dictionary of self.

who_is_carlos = {"name": "Carlos", "age": 30, "country of birth": "Mexico", "favorite language": "Python"}

# for key, value in who_is_carlos.iteritems():
    # print("My " + str(key) + " is " + str(value))


def dictionaryreader(insertdictionary):
    for key, value in insertdictionary.iteritems():
        print("My " + str(key) + " is " + str(value))

dictionaryreader(who_is_carlos)