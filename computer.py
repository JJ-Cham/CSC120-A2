class Computer:

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def refurbish(self, new_OS=None):
        """Update the price based on age, optionally update OS."""
        from datetime import date
        current_year = date.today().year
        age = current_year - self.year_made

        if age > 5:
            self.price = 200
        elif age > 3:
            self.price = 400
        else:
            self.price = 600

        if new_OS:
            self.operating_system = new_OS

    def update_price(self, new_price):
        self.price = new_price

    def update_year(self, new_year):
        self.year_made = new_year

    def upgrade_memory(self, additional_memory):
        self.memory += additional_memory

    def upgrade_hard_drive(self, additional_capacity):
        self.hard_drive_capacity += additional_capacity

    def __str__(self):
        return f"Computer: {self.description}, Processor: {self.processor_type}, Hard Drive: {self.hard_drive_capacity}GB, Memory: {self.memory}GB, OS: {self.operating_system}, Year: {self.year_made}, Price: ${self.price}"

# OUTSIDE the class
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
    print(computer)

    computer.description = "Gaming PC 2"
    print(computer)

    computer.update_price(1500) 
    print(computer)

    computer.update_year(2025)
    print(computer)

if __name__ == "__main__":
    main()
