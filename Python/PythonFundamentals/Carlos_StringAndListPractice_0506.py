#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: String and List Practice
Use only the built-in methods and functions from the previous tabs to do the following exercises.
You will find the following methods and functions useful:
• .find()
• .replace()
• min()
• max()
• .sort()
• len()
Find and Replace
In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of
the word "day". Then create a new string where the word "day" is replaced with the word "month".
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new
list containing only the first and last values in the original list. Your code should work for any list.
New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list
in half. Push the list created from the first half to position 0 of the list created from the second half. The output
should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

"""


# Find and replace
text = "It's thanksgiving day. It's my birthday,too!"
print(text, text.find("day"))

newText = text.replace("day", "month")
print(newText)

# Min and Max
x = [2, 54, -2, 7, 12, 98]

print("The minimum number of the x Array is: {0}. The maximum number is: {1}".format(min(x), max(x)))

# First and Last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]

print("Did you know the first array item is: {0}. The last array item is: {1}".format(x[0], x[-1]))

# New List
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
y = []
y.append(x[0:5])
z = x[5:-1]
for items in x[5:]:
    y.append(items)


print("The sorted list looks like: {0}. The total number of items inside the list is: {1}. The new list is: {2}"
      .format(x, len(x), y))
