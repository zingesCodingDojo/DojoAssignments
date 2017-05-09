#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many
times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer

x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1
"""
import random
from math import floor

# each toss MUST be unique. So lets greate a random number.


def getrandomnumber():
    rando_num = floor(random.random()*2)
    return int(rando_num)

print(getrandomnumber())

def cointoss(x):
    heads_counter = 0
    tails_counter = 0
    for items in range(1, x+1):
        if items == x:
            # If the random number is greater than 0, it will be heads.
            if getrandomnumber() > 0:
                heads_counter += 1
                print("Attempt #{0}. Throwing coin... it's heads! Got {1} head(s) so far and {2} tail(s) so far.\n"
                      "Ending the program, thank you!".format(items, heads_counter, tails_counter))
            # If the random number is 0, it will be tails.
            else:
                tails_counter += 1
                print("Attempt #{0}. Throwing coin... it's tails! Got {1} head(s) so far and {2} tail(s) so far.\n"
                      "Ending the program, thank you!".format(items, heads_counter, tails_counter))

        elif getrandomnumber() > 0:
            heads_counter += 1
            print("Attempt #{0}: Throwing a coin... It's a head! ... Got {1} head(s) so far and {2} tail(s) so far"
                  .format(items, heads_counter, tails_counter))
        else:
            tails_counter += 1
            print("Attempt #{0}: Throwing a coin... It's a tails! ... Got {1} head(s) so far and {2} tail(s) so far"
                  .format(items, heads_counter, tails_counter))

cointoss(100)