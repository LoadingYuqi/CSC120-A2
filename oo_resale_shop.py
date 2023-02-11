"""
    Filename: oo_resale_shop.py
    Description: An object-oriented code to run a small computer resale shop.
    Author: Yuqi Wang
    Date: 11 February 2023
"""
from computer import *

class oo_resale_shop:

    # What attributes will it need?
    ItemID: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, items):
        # Print the banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)
        self.ItemID = items

    def addComputer():
        itemID += 1

    def sellComputer():
        itemID -= 1
    
    def updatePrice(self, new_price):
        computer.price = new_price

    def updateOS(self, new_OS):
        computer.operating_system = new_OS

    # What methods will you need?

def main(): # example of taking in a computer , processing, and selling it
    first_computer = computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500) #Calling Computer class