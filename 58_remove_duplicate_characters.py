
# Remove duplicate characters from a string

s ="komalllaaalii"
result = ""
for ch in s:
    if not ch in result:
        result += ch
print("The result is: ",result)