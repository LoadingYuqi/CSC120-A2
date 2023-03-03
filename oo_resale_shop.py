"""
    Filename: oo_resale_shop.py
    Description: An object-oriented code to run a small computer resale shop.
    Author: Yuqi Wang
    Date: 11 February 2023
"""
from computer import *

class oo_resale_shop:
    """The oo_resale_shop class uses Object-Oriented programming to construct a computer resale shop where the shop can buy, sale, and refurbish computers. 
    """

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

    
    def addComputer(self, newComputer):
        """The addComputer method allows user to input the information of a new computer and add it to the inventory
        """
        self.inventory.append(newComputer)
        print ("New item", newComputer.description, "added!")
        
    def sellComputer(self, item):
        """The sellComputer method checks if a ID is in the inventory and print appropriate message
        """
        if item in self.inventory:
            print("The price of your item is", item.price, ", thank you for your purchase!") 
            self.inventory.remove(item)
        else:
            print ("Item not found.")
   
    def updatePrice(self, item, new_price):
        """The updatePrice method replace an old price of a computer with a new price 
        """
        item.price = new_price
        print("The new price of this computer is", new_price, ".")

    def updateOS(self, item, new_OS):
        """The updateOS method replace an old OS of a computer with a new one 
        """
        if item.operating_system == new_OS:
            print("This computer has the newest operating system.")
        else:
            item.operating_system = new_OS
            print("Operating system updated to", new_OS, "!")

    def refurbish(self, item):
        """The refurbish method reset price based on years of useage, update price and OS
        """
        if item.year_made < 2012:
            self.updatePrice(item, 500)
            self.updateOS(item, "macOS Big Sur")
        elif item.year_made < 2018:
            self.updatePrice(item, 1000)
            self.updateOS(item, "macOS Big Sur")
        else:
            self.updateOS(item, "macOS Big Sur")

        pass
    


def main(): # example of taking in a computer , processing, and selling it
    my_store = oo_resale_shop([], 0) #create empty store
    c:computer = computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500)
    my_store.addComputer(c) # add a new computer to the store
    my_store.refurbish(c)
    print("Would you like to buy", c.description, "? True or False:")
    response = bool(input())
    if response:
        my_store.sellComputer(c)
    else:
        print("Have a nice day!")   
    
main()