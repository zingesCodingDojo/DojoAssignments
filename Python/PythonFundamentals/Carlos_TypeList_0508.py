#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the
item is a string, concatenate it onto a new string. If it is a number, add it to a running sum.
At the end of your program print the string, the number and an analysis of what the array contains.
If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
"""
#input
l = ['magical unicorns', 19, 'hello', 98.98, 'world']
#output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# Copy
# input
l2 = [2, 3, 1, 7, 4, 12]
# output
# "The array you entered is of integer type"
# "Sum: 29"
# Copy
# input
l3 = ['magical', 'unicorns']
# output
# "The array you entered is of string type"
# "String: magical unicorns"


def typelist(x):
    b = 0
    c = ""
    for items in x:

        if isinstance(items, int) or isinstance(items, float):
            b += items

        elif isinstance(items, basestring):
            c += items + " "
    if b != 0:
        print("Did you know the sum of integers is: {0}.".format(b))

    if c != "":
        print("Did you also know the concatenation of string items is: {0}".format(c))


typelist(l)
