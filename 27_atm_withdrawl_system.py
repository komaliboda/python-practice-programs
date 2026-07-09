# ATM Withdrawal System
# This program checks whether the withdrawal is possible
# based on account balance and withdrawal conditions.

balance = 500
withdraw = int(input("Enter money: "))
if withdraw > balance :
    print("Insufficient money")
elif withdraw % 100 != 0:
    print("Enter amount in multiple of 100 ")
else:
    print("Transaction successfully")
    balance = balance - withdraw 
print("Remaining amount: ",balance)