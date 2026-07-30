s = "komali@123   "
count_digits = 0
count_letters = 0
count_spaces = 0
count_special_character = 0
for ch in s:
    if ch.isdigit():
        count_digits += 1
    elif ch.isalpha():
        count_letters += 1
    elif ch.isspace():
        count_spaces += 1
    else:
        count_special_character += 1
print("The count of  digits  is :",count_digits)
print("The count of letters is :",count_letters)
print("The count of  spaces is :",count_spaces)
print("The count of special character is :",count_special_character)
