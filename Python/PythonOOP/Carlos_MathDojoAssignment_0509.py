#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: MathDojo
HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself
(an instance of itself), we can chain methods.

PART I
Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at
least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

MathDojo().add(2).add(2, 5).subtract(3, 2).result
Copy
which should perform 0+2+(2+5)-(3+2) and return 4.

PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into
the list. It should now be able to perform the following tasks:

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
Copy
should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

PART III
Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
"""

# Part I


class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *number):
        self.number = number
        for items in self.number:
            self.result += items
        # print(self.result)
        return self

    def subtract(self, *number):
        self.number = number
        for items in self.number:
            self.result -= items
        # print(self.result)
        return self

md = MathDojo()
print(md.add(1).add(10).subtract(3, 5).add(10, 20).result)
print(md.add(1).result)


# Part II

class MathDojoTwo(object):
    def __init__(self):
        self.result = 0

    def add(self, *number):
        self.number = number
        for items in self.number:
            # print(items)
            if isinstance(items, list):
                for stuff in items:
                    self.result += stuff
            else:
                self.result += items
        # print(self.result)
        return self

    def subtract(self, *number):
        self.number = number
        for items in self.number:
            # print(items)
            if isinstance(items, list):
                for stuff in items:
                    self.result -= stuff
            else:
                self.result -= items
                # print(self.res
        return self


mp2 = MathDojoTwo()
print(mp2.add([1, 2], 1, [5, 5], 5, 5).subtract([5, 5], 5).result)


# Part III


class MathDojoThree(object):
    def __init__(self):
        self.result = 0

    def add(self, *number):
        self.number = number
        for items in self.number:
            # print(items)
            if isinstance(items, list) or isinstance(items, tuple):
                for stuff in items:
                    self.result += stuff
            else:
                self.result += items
        # print(self.result)
        return self

    def subtract(self, *number):
        self.number = number
        for items in self.number:
            # print(items)
            if isinstance(items, list) or isinstance(items, tuple):
                for stuff in items:
                    self.result -= stuff
            else:
                self.result -= items
                # print(self.res
        return self

mc3 = MathDojoThree()
print(mc3.add((5, 5), 5).subtract((5, 5), 1).result)
