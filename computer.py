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

    def __str__(self):
        return f"Computer: {self.description} Processor: {self.processor_type} Hard Drive: {self.hard_drive_capacity} Memory: {self.memory} OS: {self.operating_system} Year: {self.year_made} Price: {self.price}"
    
    def update_price(self, new_price):
        self.price = new_price

    def update_year(self, new_year):
        self.year_made = new_year

    def update_memory(self, new_memory):
        self.memory = new_memory



def main():
    description = "Gaming PC"
    processor_type = "Intel i7"
    hard_drive_capacity = 1000
    memory = 16
    operating_system = "Windows 11"
    year_made = 2025
    price = 1000
    

    computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    print(computer)

    computer.refurbish("Windows 10")
    print(computer.operating_system)


if __name__ == "__main__": 
    main()