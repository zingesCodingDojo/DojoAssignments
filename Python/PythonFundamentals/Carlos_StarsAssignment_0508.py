#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Stars
Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
Copy
draw_stars(x)should print the following in when invoked:

****
******
*
***
*****
*******
*************************
Copy
Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function.
When a string is passed, instead of displaying *, display the first letter of the string according to the example
below. You may use the .lower() string method for this part.

For example:

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
Copy
draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
"""

# Creating function to take in a list of number and prints out *.


def draw_stars(arr):
    for items in range(len(arr)):
        stars = ""
        # print(items, arr[items])
        for stuff in range(arr[items]):
            stars += "*"
        print(stars)

x = [4, 6, 1, 3, 5, 7, 25]

# draw_stars(x)

# Part II


def draw_better_stars(arr):
    for items in range(len(arr)):
        stars = ""
        newchars = ""
        # print(items, arr[items])
        if isinstance(arr[items], basestring):
            for chars in range(len(arr[items])):
                newchars += arr[items].lower()[0]
        else:

            for stuff in range(arr[items]):
                stars += "*"
        print(stars+newchars)

    return(stars+newchars)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_better_stars(x)