from computer import *


class ResaleShop:

    # What attributes will it need?
    #inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = inventory
        

    # What methods will you need?
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        #1. call Computer(...) constructor
            #to create a new computer instance
        new_computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        #2. call inventory.append(...) to add the new computer to the inventory
        self.inventory.append(new_computer)
        #- sell, buy, updates, storing info of the inventory in a list
        #3. return the computer's ID
        return new_computer
     
    def sell(self, computer_index):
        if 0 <= computer_index < len(self.inventory):
            sold_computer = self.inventory.pop(computer_index)
            print(f"Sold computer: {sold_computer}")
        else:
            print("Error: Invalid index. No computer sold.")

    def refurbish(self, computer_index, new_OS):
        if 0 <= computer_index < len(self.inventory):
            self.inventory[computer_index].refurbish(new_OS)
            print(f"Computer {computer_index} updated to {new_OS}")
        else:
            print("Error: Invalid index. No computer updated.")

    def print_inventory(self):
        if self.inventory:
            for i, computer in enumerate(self.inventory):
                print(f"Index {i}: {computer}")
        else:
            print("Inventory is empty.")

    def print_details(self):
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