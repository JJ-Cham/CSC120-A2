from computer import *


class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, inventory=None):
        self.inventory = inventory
        

    # What methods will you need?
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        #1. call Computer(...) constructor
            #to create a new computer instance
        new_computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)

        #2. call inventory.append(...) to add the new computer to the inventory
        self.inventory.append(new_computer)
        #- sell, buy, updates, storing info of the inventory in a list 
    def sell(self):
        #1. call inventory.pop(...) to remove the computer from the inventory

        Computer.inventory.pop(self)

    def refurbish(self):
        #1. call Computer.refurbish(...) to update the computer's OS
        Computer.refurbish(self, new_OS)

    def print_inventory(self):
        #1. print out the inventory
        print(self.inventory)

    def __str__(self):
        return f"Computer: {self.description} Processor: {self.processor_type} Hard Drive: {self.hard_drive_capacity} Memory: {self.memory} OS: {self.operating_system} Year: {self.year_made} Price: {self.price}"
    
    def main():
        description = "Gaming PC"
        processor_type = "Intel i8"
        hard_drive_capacity = 1000
        memory = 16
        operating_system = "Windows 12"
        year_made = 2024
        price = 1000

        computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        print(computer.refurbish("Windows 11"))

    if __name__ == "__main__": 
        main()