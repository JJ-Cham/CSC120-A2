class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    
# What methods will you need?
    def refurbish(self, new_OS):
        self.operating_system = new_OS

    def print_details(self):
        return f"Computer: {self.description}, Processor: {self.processor_type}, Hard Drive: {self.hard_drive_capacity}GB, Memory: {self.memory}GB, OS: {self.operating_system}, Year: {self.year_made}, Price: ${self.price}"
    
    def update_price(self, new_price):
        self.price = new_price

    def update_year(self, new_year):
        self.year_made = new_year

    def upgrade_memory(self, additional_memory):
        self.memory += additional_memory
    
    def upgrade_hard_drive(self, additional_capacity):
        self.hard_drive_capacity += additional_capacity
    
    def detailed_info(self):
        return {
            "description": self.description,
            "processor_type": self.processor_type,
            "hard_drive_capacity": self.hard_drive_capacity,
            "memory": self.memory,
            "operating_system": self.operating_system,
            "year_made": self.year_made,
            "price": self.price
        }



# Now, let's test it out!
def main():
    description = "Gaming PC"
    processor_type = "Intel i7"
    hard_drive_capacity = 1000
    memory = 16
    operating_system = "Windows 11"
    year_made = 2013
    price = 1000
    

    computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    print(computer)

    computer.refurbish("Windows 10")
    print(computer.operating_system)

    computer.description = "Gaming PC 2"
    print(computer.description)

    computer.update_price(1500) 
    print(computer.price)

    computer.update_year(2025)
    print(computer.year_made)

if __name__ == "__main__": 
    main()