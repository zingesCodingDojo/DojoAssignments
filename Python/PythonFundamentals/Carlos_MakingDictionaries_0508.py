#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary where the first list contains keys
and the second values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:
"""
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "CRAP"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "PYTHON", "PYTHON"]
"""
Copy
Here's some help starting your function.

def make_dict(arr1, arr2):
  new_dict = {}
  # your code here
  return new_dict
Copy
Hacker Challenge:
If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.
"""


def make_dict(arr1, arr2):
    new_dict = {}
    counter = 0
    for items in arr1:
        new_dict[items] = arr2[counter]
        counter += 1

    print(new_dict)
    return new_dict

# make_dict(name, favorite_animal)

# Hacker Challenge


def make_complex_dict(arr1, arr2):
    new_dict = {}
    counter = 0
    if len(arr1) > len(arr2):
        print("Using first plugged array, since it is longer.")
        while len(arr2) != len(arr1):
            arr2.append("PLACEHOLDER")
        for items in arr1:
            new_dict[items] = arr2[counter]
            counter += 1
    elif len(arr1) < len(arr2):
        print("Using second plugged array, since it is longer.")
        while len(arr1) != len(arr2):
            arr1.append("PLACEHOLDER")
        for items in arr2:
            new_dict[items] = arr1[counter]
            counter += 1
    else:
        print("Seems like arrays are the same length... default to the code of the first section.")
        for items in arr1:
            new_dict[items] = arr2[counter]
            counter += 1
    print(new_dict)
    return new_dict

make_complex_dict(name, favorite_animal)