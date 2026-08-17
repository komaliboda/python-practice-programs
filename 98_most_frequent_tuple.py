# Find the most frequently occurring element in a tuple

t = (10,20,30,40,10,20)

most_element = 0
most_count = 0

for i in t:
    count = t.count(i)
    
    if count > most_count:
        most_count = count
        most_element = i
        
print(most_element,most_count)