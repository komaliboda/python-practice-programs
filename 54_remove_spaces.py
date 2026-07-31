# Removing spaces in the string 

s ="komali vishnu siddu koti"
result = ""
for ch in s:
    if not ch.isspace():
        result += ch
print(result)
    