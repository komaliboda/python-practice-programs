# Find the first duplicate element in a tuple

t =(10,30,20,10)

for i in t:
    if t.count(i) > 1:
        print(i)
        break
