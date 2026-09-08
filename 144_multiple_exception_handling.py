# Handle ValueError and ZeroDivisionError using try and except

try:
    number = int(input("Enter a number: "))
    result = 10/number

except ValueError:
    print("Enter a valid number ")

except ZeroDivisionError:
    print("Number cannot be zero ")

print(result)