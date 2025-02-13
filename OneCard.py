class OneCard: 
    
    owner: str
    balance: float 

    def __init__(self, name:str, amt:float):
        self.owner = name
        self.balance = amt

    def deposit(self, amt:float):
        self.balance = amt

    def deposit(self, amt:float):
        self.balance += amt

    def canAfford(self, amt:float):
        return self.balance >= amt
    

def main():
    myCard: OneCard = OneCard("Jordan", 3.00)
    print(myCard)
    myCard.deposit(10)
    print("This card belongs to", myCard.owner)
    print(myCard.owner, "has $", myCard.balance, "available.")
    print(myCard.canAfford(4))

    # absCard: OneCard = OneCard("Ab", 30.00)
    # print(absCard)
    # print("This card belongs to", absCard.owner)
    # print(absCard.owner, "has $", absCard.balance, "available.")

if __name__ == "__main__":
    main()
    