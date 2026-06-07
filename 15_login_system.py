
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