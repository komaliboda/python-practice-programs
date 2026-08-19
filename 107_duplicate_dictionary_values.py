# Find duplicate values in a dictionary

s = {"a":10,
     "b":20,
    "c":30,
    "d":40,
    "e":30
}
seen = []
for value in s.values():
    
if value in seen:
        print(value)
    else:
        seen.append(value)