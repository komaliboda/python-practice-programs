# Rotate a tuple one position to the right

t =(10,30,20,10)

new_t = (t[-1],)+(t[:-1])

print(new_t)