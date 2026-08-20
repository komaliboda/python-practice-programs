# Find common keys between two dictionaries

dict1 = {"a":10,"b":20,"c":30}
dict2 = {"d":20,"b":300,"a":10}
temp = {}

for key,values in dict1.items():
    if key in dict2:
        temp[key] = values
print(temp)