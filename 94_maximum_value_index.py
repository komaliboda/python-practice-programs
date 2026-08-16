# Find the maximum value and its index in a tuple

t =(10,30,20)

max_value = t[0]
max_index = 0

for i in range(len(t)):
    if t[i] > max_value:
        max_value = t[i]
        max_index = i

print(max_index,max_value)