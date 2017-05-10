#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Class Structure
You can easily create a class in Python by typing the keyword class followed by the name of your class and (object).

class User(object):
    pass
Copy
You should notice that we define one parameter object. When the parameter for a class is object it simply means that
this class inherits from the object class. We'll get into inheritance a little more later on. You'll notice the keyword
pass in the body - it is used as a placeholder where some code is required. It means do nothing.

More generally, a class looks like this:

class ClassName(object):
  #attributes and methods here (we'll talk more about these in a moment)
Copy
Think of the class as a blueprint for creating something. Once we've finished our blueprint we can create instances of
this class. The User class we defined above is a blueprint for creating users. We create a new instance by using the
class name as if it were a function. Let's go ahead and make instances of our human class

michael = User()
anna = User()
Copy
Let's print these and see what the output is:

The output we see here gives you information about what class your object belongs to and where it is stored in memory.
Later, we'll talk about how to manipulate the way this output is displayed.

It can be helpful to think of a class as a blueprint and an object as the thing we make based on that blueprint.

Classes include two types of things:

Attributes: Characteristics shared by all instances of the class type. Take our User class, for example. All users have
a name and an email. You might be wondering how each user can have a different name and email. We'll show you in the
following tab.
Methods: Actions that an object can perform. A user, for example, might be able to make a purchase. A method is like a
function that belongs to a class. It's some instructions that will only work when called on an object that has been
created from that class. We'll show you how shortly.
In the following tabs we'll talk more about attributes and methods. Remember, objects have two important features:
storage of information and ability to execute some logic.
"""