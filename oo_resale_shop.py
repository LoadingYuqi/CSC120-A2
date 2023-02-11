"""
    Filename: oo_resale_shop.py
    Description: An object-oriented code to run a small computer resale shop.
    Author: Yuqi Wang
    Date: 11 February 2023
"""
from computer import *
from typing import Dict, Union, Optional

class oo_resale_shop:

    inventory: list = []
    itemID: int = 0

    def __init__(self, stock, items):
        self.inventory = stock
        self.itemID = items
        # Print the banner

        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    def addComputer(self, name, processor, hardDrive, memoryInt, operatingSystem, yearMade, priceInt):
        newComputer = computer(name, processor, hardDrive, memoryInt, operatingSystem, yearMade, priceInt)
        self.inventory.append(newComputer)
        self.itemID += 1
        print ("Item ", self.itemID, " added!")

    def sellComputer(self, item):
        itemID -= 1
    
    def updatePrice(self, new_price):
        computer.price = new_price

    def updateOS(self, new_OS):
        computer.operating_system = new_OS


def main(): # example of taking in a computer , processing, and selling it
    my_store = oo_resale_shop([], 0)
    my_store.addComputer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500) # Adding a new computer
    
main()