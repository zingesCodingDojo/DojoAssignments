#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are
identical print "The lists are the same". If they are not identical print "The lists are not the same."
Try the following test cases for lists one and two:
"""
list_one = [1, 2, 5, 6, 2]
list_two = [1, 2, 5, 6, 2]
# Copy
list_three = [1,  2,  5,  6,  5]
list_four = [1, 2, 5, 6, 5, 3]
# Copy
list_five = [1, 2, 5, 6, 5, 16]
list_six = [1, 2, 5, 6, 5]
# Copy
list_seven = ['celery', 'carrots', 'bread', 'milk']
list_eight = ['celery', 'carrots', 'bread', 'cream']


def comparearrays(x, y):
    counter = 0
    if len(x) == len(y):
        print("Both lists have same len length! Lets see if each index value is the same..")
        for items in range(len(x)):
            # print(x[items])
            if x[items] == y[items]:
                counter += 1
            else:
                print("ABORT! BREAK! We were lied to! Lists are NOT the same.")
                break
    else:
        print("len of lists does not match... so, please try new lists.")
    if counter == len(x):
        print("Lists were the same")

comparearrays(list_one, list_two)
