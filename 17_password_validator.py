#--------------------------------------
#project : password length checker
#description : validate password strength 
#--------------------------------------
while True:
    password = input("Enter your password  : ")
    if len(password) < 8 :
        print("password must be 8 charactes long")
    elif password.isalpha() :
        print("password must include numbers ")
    elif password.isdigit():
        print("password must include alphabet ")
    elif password.islower():
        print("one letter must be captial")
    else :
        print("strong password ")
        break