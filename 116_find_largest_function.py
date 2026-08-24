# Find the largest number using a function and *args

def maximum_number(*args):
    maximum = 0
    for i in args:
        if i > maximum:
            maximum = i
    return maximum 
print(maximum_number(10,20,30,40))