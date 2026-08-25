# Check whether a string is a palindrome using a function

def palindrome(text):
    rev = ""
    for i in text:
        rev = i+rev
    if text == rev:
        return True
    else:
        return False
    return rev
print(palindrome("madam"))