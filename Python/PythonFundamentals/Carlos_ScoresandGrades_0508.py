#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your
function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A
The result should be like this:

Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!
Copy
Hint: Use the python random module to generate a random number

import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint()
"""

import random
from math import floor, ceil

# lets generate random numbers here:


def getrandom():
    # I am going to ROUND DOWN. Because we are mean.
    randomnum = floor(random.random() * 100 + 1)
    if randomnum in range(1, 60):
        print("Score is: {0}. Your grade is: F".format(randomnum))
    elif randomnum in range(61, 70):
        print("Score is: {0}. Your grade is: D".format(randomnum))
    elif randomnum in range(71, 80):
        print("Score is: {0}. Your grade is: C".format(randomnum))
    elif randomnum in range(71, 90):
        print("Score is: {0}. Your grade is: B".format(randomnum))
    elif randomnum in range(91, 101):
        print("Score is: {0}. Your grade is: A".format(randomnum))
    # print(randomnum)
    return randomnum

getrandom()
