#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Multiples, Sum, Average
This assignment has several parts. All of your code should be in one file that is well commented to indicate what
each block of code is doing and which problem you are solving. Don't forget to test your code as you go!

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to
do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""


# Multiples, Part I
for items in range(0, 1001, 2):
    if items == 0:
        pass
    else:
        print(items)

# Multiples, Part II
for items in range(0, 1000001, 5):
    if items == 0:
        pass
    else:
        print(items)

# Sum List
a = [1, 2, 5, 10, 255, 3]
b = 0
for items in a:
    b += items
print(b)

# Average List
a = [1, 2, 5, 10, 255, 3]
b = 0
for items in a:
    b += items
c = b/len(a)
print(c)
