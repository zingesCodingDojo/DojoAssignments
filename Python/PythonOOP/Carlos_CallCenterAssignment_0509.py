#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Assignment: Call Center
You're creating a program for a call center. Every time a call comes in you need a way to track that call.
One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call():
Create your call class with an init method. Each instance of Call() should have a few attributes:

- unique id

- caller name

- caller phone number

- time of call

- reason for call

The call class should have a display method that prints all call attributes.

CallCenter():
Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:

- calls: should be a list of call objects

- queue size: should be the length of the call list

The call center class should have an add method that adds a new call to the end of the call list

The call center class should have a remove method that removes the call from the beginning of the list (index 0).

The call center class should have a method called info that shows the name and phone number for each
call in the queue as well as the length of the queue.

You should be able to test your code to prove that it works. Remember to build one piece at a time and
test as you go for easier debugging!

Ninja Level: add a method to call center class that can find and remove a call from the queue according to
the phone number of the caller.

Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls
get out of order? Add a method to the call center class that sorts the calls in the queue according to time
of call in ascending order.
"""
from time import strftime, sleep
import random
import math


def random_id():
    """
    Generate a new UNIQUE ID for the caller.
    :return:
    """
    return int(math.floor(random.random() * 500001))


def variable_time():
    """
    Generate a unique time for the caller.
    :return:
    """
    return strftime("%a, %d %b %Y %H:%M:%S")


class Call(object):
    def __init__(self, name, phone_number, call_reason):
        self.id = random_id()
        self.name = name
        self.phone_number = phone_number
        sleep(1)
        self.call_time = variable_time()
        self.call_reason = call_reason

    def display_info(self):
        print("Unique ID: {0}.\nName of caller: {1}.\nPhone Number: {2}.\nCall time: {3}.\nCall reason: {4}.\n"
              .format(self.id, self.name, self.phone_number, self.call_time, self.call_reason))
        return self

first_call = Call("Mandeep", "(206)555-1234", "Emergency")
# first_call.display_info()

second_call = Call("Ed", "(206)800-1234", "Bored")
# second_call.display_info()

third_call = Call("Danger", "(206)000-1234", "Broken Bone")
# third_call.display_info()


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add_newcall(self, calls):
        self.calls.append(calls)
        # print(self.calls) This was used to test whether a new call was being added correctly.
        return self

    def call_duration(self):
        """
        How long was was the call?
        :return:
        """
        for items in self.calls:
            print(items.call_time)
        return self

    def remove_call(self):
        """
        Remove the call from the begining of the list, index 0.
        :return:
        """
        self.calls.remove(self.calls[0])
        return self

    def queue_duration(self):
        """
        Shows name and phone number for each call in the queue as well as length of queue.
        :return:
        """
        for items in self.calls:
            print("Caller: {0}.\nHas been on hold for: {1} minutes and {2} seconds"
                  .format(items.name, int(variable_time()[-5:-3]) - int(items.call_time[-5:-3]),
                          int(variable_time()[-2:]) - int(items.call_time[-2:])))
        return self

    def remove_based_on_phonenumber(self):
        """
        Will remove callers based on phone number. It will remove callers with smaller integer values.
        Phone numbers are sent to a new list where they are sorted and then the list is referenced back to
        the original list and removes the list item that matched with the lowest phone number.
        :return:
        """
        phone_list = []
        for items in self.calls:
            phone_list.append(items.phone_number)

        for stuff in sorted(phone_list):
            for items in self.calls:
                if stuff in items.phone_number:
                    self.calls.remove(items)
                    return self

        return self

check_mycallls = CallCenter()
check_mycallls.add_newcall(first_call).add_newcall(second_call).add_newcall(third_call)
# check_mycallls.call_duration().remove_call().call_duration()

check_mycallls.queue_duration().remove_based_on_phonenumber().queue_duration()