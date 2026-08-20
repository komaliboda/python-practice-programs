# Find common keys with different values in two dictionaries

dict1 = {"a":100,"b":20,"c":30}
dict2 = {"d":20,"b":300,"a":10}
temp = {}

for key,values in dict1.items():
    if key in dict2:
        if values != dict2[key]:
            print(key)

