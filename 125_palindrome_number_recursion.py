# Check whether a number is a palindrome using recursion

def reverse_num(n, rev = 0):
    if n == 0:
        return rev
    return reverse_num(n//10,rev*10+n%10)

n = 111

if n == reverse_num(n):
    print("palindrome ")
else:
    print("Not palindrome ")
