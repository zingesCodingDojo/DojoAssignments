#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Product
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product class should have these attributes:
Price
Item Name
Weight
Brand
Cost
Status: default "for sale"
Product class should have these methods:
Sell: changes status to "sold"
Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because
it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark
it as for sale. If the box has been opened set status to used and apply a 20% discount.
Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
"""


class Product(object):
    def __init__(self, price=int(), item_name=str(), weight=int(), brand=str()):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = int()
        self.tax = 1.098
        self.status = "for sale"
        self.add_tax()

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self):
        self.cost = self.price * self.tax
        return self

    def returned_to_store(self, new=False):
        self.status = "defective"

        if new:
            self.cost = self.price * (1 - 0.20)
        else:
            self.price = 0
            self.cost = self.price
        return self

    def display_info(self):
        print("Your product costs: {0}.\nYour product name: {1}.\nYour product weight: {2}lb.\n"
              "Your product brand: {3}.\nYour product status is: {4}.\n"
              "Your total cost: {5}.".format(self.price, self.item_name,
                                             self.weight, self.brand, self.status, self.cost))
        return self


weird_product = Product(100, "String", 5, "Generic")
weird_product.display_info()
weird_product.returned_to_store(new=True).display_info()
weird_product.returned_to_store(new=False).display_info()
