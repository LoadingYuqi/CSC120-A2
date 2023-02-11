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

        # the storage space and number of items in the store
        self.inventory = stock
        self.itemID = items

        # Print the banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    # The addComputer method allows user to input the information of a new computer and add it to the inventory
    def addComputer(self, name, processor, hardDrive, memoryInt, operatingSystem, yearMade, priceInt):
        newComputer = computer(name, processor, hardDrive, memoryInt, operatingSystem, yearMade, priceInt)
        self.inventory.append(newComputer)
        self.itemID += 1
        print ("Item ", self.itemID, " added!")
        
    # The sellComputer method checks if a ID is in the inventory and print appropriate message
    def sellComputer(self, ID):
        if len(self.inventory) >= ID:
            print("The price of your item is ")
        else:
            print ("Item not found.")
   
        
    # The updatePrice method replace an old price of a computer with a new price 
    def updatePrice(self, new_price):
        computer.price = new_price

     # The updateOS method replace an old OS of a computer with a new one 
    def updateOS(self, new_OS):
        computer.operating_system = new_OS


def main(): # example of taking in a computer , processing, and selling it
    my_store = oo_resale_shop([], 0) #create empty store
    my_store.addComputer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500) # add a new computer to the store
    item_to_buy = int(input("Which item would you like to buy? :")) # take in an item ID
    #my_store.sellComputer(item_to_buy)
    my_store.sellComputer(item_to_buy)
main()