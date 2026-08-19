# Group dictionary keys based on their values

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

grouped = {}

for key, value in data.items():
    if value not in grouped:
        grouped[value] = [key]
    else:
        grouped[value].append(key)

print(grouped)