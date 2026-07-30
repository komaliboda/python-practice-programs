# checks whether the string is palindrome or not
s = input("Enter something: ")
rev = ""
for ch in s:
    rev = ch+rev
print(rev)
if s == rev:
    print("Palindrome ")
else:
    print("not Palindrome ")