#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Animal
Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child
classes, Dog and Dragon.

Objective
The objective of this assignment is to help you understand inheritance. Remember that a class is more than just
a collection of properties and methods. If you want to create a new class with attributes and methods that are already
defined in another class, you can have this new class inherit from that other class (called the parent) instead of
copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent
class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja /
Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same
parent class.

Animal Class
Create a class called Animal with the following attributes: name, and health. Give the Animal the following three
methods: walk, run, and displayHealth. Give a new Animal 100 health when it gets created. When the walk() method is
invoked, have the health decrease by 1. When the run() method is invoked, have the health decrease by 5. When the
displayHealth() method is invoked, display on screen the name of the Animal and the health.

Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm
that the health attribute has changed.

Dog Class
Create a class called Dog that inherits everything that the Animal does, except the Dog class should have a default
health of 150 and a new method called pet(), which increases the health by 5. Have the Dog walk() three times, run()
twice, pet() once, and have it displayHealth().

Dragon Class
Finally, create a class called Dragon that also inherits everything from Animal. The Dragon class should have the
default health be 170 and a new method called fly(), which decreased the health by 10. Have the Dragon walk() three
times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth() function is called,
it should say 'this is a dragon!' before it displays the default information. You can achieve this by calling the
parent's displayHealth() function.

Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and it's displayHealth()
is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
"""


class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("Your Animal name is: {0}.\nYour health is at: {1}".format(self.name, self.health))
        return self

first_animal = Animal("BadAnimal", 100)

first_animal.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name=name, health=150)

    def pet(self):
        self.health += 5
        return self

first_dog = Dog("TerribleDog")
first_dog.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name=name, health=170)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        Animal.display_health(self)
        print("this is a dragon!")
        return self

first_dragon = Dragon("Destroyer")
first_dragon.walk().walk().walk().run().run().fly().fly().display_health()
# first_dragon.fly().fly().display_health()

# first_dog.fly()  ---- AttributeError: 'Dog' object has no attribute 'fly'


class MadeUpAnimal(Animal):
    def __init__(self, name):
        super(MadeUpAnimal, self).__init__(name=name, health=25)


temp_animal = MadeUpAnimal("Made Up Animal!")
temp_animal.display_health()
# temp_animal.pet()  ---- AttributeError: 'MadeUpAnimal' object has no attribute 'pet'
# temp_animal.fly()  ---- AttributeError: 'MadeUpAnimal' object has no attribute 'fly'

