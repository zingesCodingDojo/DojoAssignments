#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Checkerboard
Write a program that prints a 'checkerboard' pattern to the console.

Your program should require no input and produce console output that looks like so:

* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
Copy
Each star or space represents a square. On a traditional
checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces.
The goal is to repeat a process several times. This should make you think of looping.
"""


def checkerboard():
    columns = 15
    rows = 15
    evens = ""
    odds = ""
    newthing = ""
    for items in range(rows):
        if items % 2 == 0:
            evens += "+"
            odds += " "
        else:
            evens += " "
            odds += "+"
    for stuff in range(columns):
        if stuff % 2 == 0:
            newthing += evens + "\n"
        else:
            newthing += odds + "\n"
    # print(evens)
    # print(odds)
    print(newthing)

checkerboard()