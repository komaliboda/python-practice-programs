# Create and handle a custom exception for negative age

class InvalidAgeError(Exception):
    pass
age = -5
try:
    if age < 0:
        raise InvalidAgeError("age can't be negative ")

except InvalidAgeError:
    print("age can be positive")
 