#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Names
Write the following function.

Part I
Given the following list:
"""
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
"""
Copy
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
Copy
Part II
Now, given the following dictionary:
"""
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }
"""
Copy
Create a program that prints the following format (including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
Copy
Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs.
Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement
of any web application.
"""

# Making a function to print out values of lists.


def gimmevalues(insertlist):
    for items in insertlist:
        getnames = ""
        for key, values in items.iteritems():
            getnames += values + " "
        print(getnames)

gimmevalues(students)

# Making a function to print out values of a dictionary and its sub values and total lens of sub values.


def gimmedeepvalues(innerdictionary):
    for key, values in innerdictionary.iteritems():
        makingnewheader = ""
        makingnewheader += key
        print(makingnewheader)
        counter = 0
        for items in values:
            addingnames = ""
            getmylen = 0
            for junk, stuff in items.iteritems():
                addingnames += stuff + " "
                getmylen += len(stuff)
            counter += 1
            print("{0} - {1}- {2}".format(counter, addingnames, getmylen))


gimmedeepvalues(users)
