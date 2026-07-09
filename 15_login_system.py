
#--------------------------------------
#project : login system 
#Description : checks user password and user name
#--------------------------------------

username = input("Enter your name : ")
password = input("Enter your password 🔑: ")
if username == "komali" and password == "komali123":
    print("Login successfully ")
    print("welcome" ,username)
else:
    print("Invalid username or password")



# Login System
# This program verifies the username and password using nested if statements.

user_name = input("Enter  user name: ")

if user_name == "komali":
    password = input("Enter your password ")
    if password == "komali@112":
        print("Login Successfully ")
    else:
        print("wrong password")
else:
    print("User name not found")
