from computer import *
class ResaleShop:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def buy(self, computer: Computer):
        self.inventory.append(computer)

    def sell(self, computer_index):
        if 0 <= computer_index < len(self.inventory):
            sold_computer = self.inventory.pop(computer_index)
            print(f"Sold computer: {sold_computer}")
        else:
            print("Error: Invalid index. No computer sold.")

    def refurbish(self, computer_index, new_OS=None):
        if 0 <= computer_index < len(self.inventory):
            self.inventory[computer_index].refurbish(new_OS)
            print(f"Computer {computer_index} refurbished.")
        else:
            print("Error: Invalid index. No computer updated.")

    def print_inventory(self):
        if self.inventory:
            for i, computer in enumerate(self.inventory):
                print(f"Index {i}: {computer}")
        else:
            print("Inventory is empty.")


# OUTSIDE the class
def main():
    # Create a shop
    shop = ResaleShop()

    # Create a computer
    description = "Gaming PC"
    processor_type = "Intel i8"
    hard_drive_capacity = 1000
    memory = 16
    operating_system = "Windows 12"
    year_made = 2024
    price = 1000

    computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)

    # Buy the computer (add to inventory)
    shop.buy(computer)

    # Print inventory
    shop.print_inventory()

    # Refurbish the computer
    shop.refurbish(0, "Windows 11")

    # Print inventory again
    shop.print_inventory()

if __name__ == "__main__":
    main()
