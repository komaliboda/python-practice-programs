# Handle insufficient balance using a custom exception

class InsufficientBalance(Exception):
    pass
balance = 1000
withdraw = int(input("enter withdraw amount: "))

try:
    if withdraw > balance:
        raise InsufficientBalance("insufficient balance ")
    else:
        balance = balance - withdraw 
except InsufficientBalance:
    print("enter amount within balance")
finally:
    print(balance)
    
    