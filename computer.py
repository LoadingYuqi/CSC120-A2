"""
    Filename: computer.py
    Description: An object-oriented code to create a computer for a computer resale shop.
    Author: Yuqi Wang
    Date: 11 February 2023
"""
class computer:

    # Attributes of a computer in the store
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = ""
    memory: int = ""
    operating_system: str = ""
    year_made: int = ""
    price: int = ""

    # The __init__ constructs an object in the computer store
    def __init__(self, descriptionText, processor, hardDrive, memoryInt, operatingSystem, yearMade, priceInt):
        self.description = descriptionText
        self.processor_type = processor
        self.hard_drive_capacity = hardDrive
        self.memory = memoryInt
        self.operating_system = operatingSystem
        self.year_made = yearMade
        self.price = priceInt

    # What methods will you need?