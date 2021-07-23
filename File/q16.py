#Write a python program to check whether the string is Palindrome or not.
def check(s):
    if s==s[::-1]:
        return True
    else:
        return False


s=input("Enter a string to check pallindrome: ")
c=check(s)
if c is True:
    print(s,"is Pallindrome")
else:
    print(s,"is NOT a Pallindrome")    