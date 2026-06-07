#--------------------------------------
#project : number analysis 
#Description : checks  number positive/negative and even/odd
#--------------------------------------
num = int(input("Enter a number : "))
if num == 0:
    print("zero ")
elif num > 0:
    if num%2 == 0:
        print("positive even ")
    else:
        print("negative odd ")
else:
    if num%2 == 0:
        print("positive even ")
    else:
        print("negative odd ")