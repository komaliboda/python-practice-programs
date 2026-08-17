# Find the first non-repeating element in a tuple

t = (10,20,30,40,10,20)

for i in t:
    if t.count(i) <= 1:
        print(i)
        break
        