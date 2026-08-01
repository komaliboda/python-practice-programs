# Check whether two strings are anagrams

s1 = input("enter the string 1").lower()
s2 = input("enter the string 2 ").lower()
if len(s1) == len(s2):
    for i in s1:
        if s1.count(i) != s2.count(i):
            print("Not anagram ")
            break
    else:
        print("anagram ")