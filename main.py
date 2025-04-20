# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish


""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""

def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():

    # First, let's make a Computer object
    computer = create_computer(
        description="Mac Pro (Late 2013)",
        processor_type="3.5 GHz 6-Core Intel Xeon E5",
        hard_drive_capacity=1024,  
        memory=64,                 
        operating_system="macOS Big Sur",
        year_made=2013,
        price=1500
    )

    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying:", computer.description)
    print("Adding to inventory...")
    shop.buy(computer)
    print("Done.\n")

    # Check inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Refurbish it (update OS + price)
    new_OS = "macOS Monterey"
    print(f"Refurbishing first computer, updating OS to {new_OS}...")
    shop.refurbish(0, new_OS)  # 0 because it's the first computer
    print("Done.\n")

    # Check inventory again
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Sell it
    print("Selling first computer...")
    shop.sell(0)
    print("Done.\n")

    # Check inventory one last time
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

# Run the main function
if __name__ == "__main__":
    main()
