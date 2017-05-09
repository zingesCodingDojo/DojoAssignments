#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Fun with Functions
Create a series of functions based on the below descriptions.

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program
print the number of that iteration and specify whether it's an odd or even number.

Your program output should look like below:

Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
Copy
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16])
and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:

a = [2,4,10,16]
Copy
Then:

b = multiply(a, 5)
print b
Copy
Should print [10, 20, 50, 80 ].

Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return
the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the
number in the original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
"""

# Odd/Even


def odd_even(start, end):
    for x in range(start, end):
        if x % 2 == 0:
            print("Number is: {0}. This is an even number.".format(x))
        else:
            print("Number is: {0}. This is an odd number.".format(x))
# Calling the function will produce a large print statement. Please remove comment # to see what happens!
# odd_even(1, 2001)


# Multiply


def multiply(arr, multiple):
    for items in range(len(arr)):
        arr[items] *= multiple
    print(arr)
    return arr

testlist = [1, 2, 3, 4, 5, 6, 7, 8]
# multiply(testlist, 5)
multipliedlist = multiply(testlist, 2)
# print(multipliedlist)

# Hacker Challenge


def layered_multiples(arr):
    new_array = []
    for items in range(len(arr)):
        new_array.append([])
        for stuff in range(arr[items]):
            new_array[items].append(1)
    #print(new_array)
    return new_array

layered_multiples(multipliedlist)