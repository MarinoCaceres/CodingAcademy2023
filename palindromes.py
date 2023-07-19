s = input("Insert text to test if it is a palindrome: ")

if s[::-1] == s[::1]:
    print("The text {",s,"} is a palindrome")

else:
    print("The text {",s,"} is NOT a palindrome")