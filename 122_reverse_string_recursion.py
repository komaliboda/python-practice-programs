# Reverse a string using recursion

def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:])+text[0]

print(reverse("hello"))