

class OneCard {

    String owner;
    float balance;


    public OneCard(String owner, float amt) {
        this.owner = name;
        this.balance = amt;
    }

    public void deposit(float amt){
        this.balance += amt;
    }

    private boolean canAfford(float amt){
        return this.balance >= amt;
    }

    public spend(float amt){
        if (canAfford(amt)){
            this.balance -= amt;
        } else{
            System.out.println("Insufficient funds please deposit money.");             
        }
    }
}


public static void main(String[] args) {
    OneCard myCard = new OneCard("Jordan", amt:3.00);
    System.out.println()
}