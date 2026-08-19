# Reverse the keys and values of a dictionary

s = {
    "student" : "komali",
     "age" : 19,
    "studying " : "BTECH"
    }
new_dict = {}

for key,values in s.items():
    new_dict[values] = key

print(new_dict)
