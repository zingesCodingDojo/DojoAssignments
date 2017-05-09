#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character,
and prints a new list of all the strings containing that character.

Here's an example:
"""
# input
l = ['hello','world','my','name','is','Anna']
# char = 'o'
# output
n = ['hello','world']
# Copy
# Hint: how many loops will you need to complete this task?


def findcharacters(randolist, char):
    """
    The purpose of this function is to accept a list of strings and a single character string. It will then
    see if the param char is inside param randolist. If char in randolist, then a new list will be returned with
    all instances of the index where char was found in randolist.
    :param randolist:
    :param char:
    :return:
    """
    newlist = []
    for items in randolist:
        if char in items:
            newlist.append(items)
    print(newlist)
    return newlist

findcharacters(l, "o")
