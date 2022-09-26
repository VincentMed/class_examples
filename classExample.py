# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:27:37 2022

@author: Vincent Medrano
"""

'''
We have a class defined for vehicles.
Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
and car2 to be a blue van named Jump worth $10,000.00.
'''

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# car1 object created in the Vehicle() class.
car1 = Vehicle()
# assign Fer to car1's name
car1.name = "Fer"
# assign color to car1
car1.color = "red"
# assign the type of car to car1
car1.kind = "convertible"
# assign the price to car1
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())