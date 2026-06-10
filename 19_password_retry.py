#--------------------------------------
#project : password retry system 
#description : allows only 3 times
#--------------------------------------

password = "komali@123"
chances = 3
while chances > 0:
    user_password = input("enter password 🔑 ")
    if password == user_password:
        print("login successfully ")
        break
    else:
        chances -= 1
        print("wrong password ")
        print("remaining chances : ",chances)
if chances == 0:
    print("Account locked 🔒")