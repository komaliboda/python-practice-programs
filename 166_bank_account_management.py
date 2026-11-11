# Bank Account Management System using OOP
# Demonstrates classes, objects, constructors, class variables,
# instance variables, deposit, withdrawal, and balance checking.

class bank:
    bank_name = "SBI"
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount : ",amount)
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print("Remaining balance: ", self.balance)
        else:
            print("Insufficient balance ")
    def check_balance(self):
        print("Available balance:", self.balance)
        
    def display(self):
        print("Account holder name is : ",self.account_holder)
        print("Bank is : ",bank.bank_name)
        print("The total balance is : ",self.balance)

c1 = bank("komu",18)
c2 = bank("vishnu",10)
c1.deposit(200)
c1.withdraw(1800)
c1.check_balance()
c1.display() 
