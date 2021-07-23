#Write a python program that switches the values stored in the variables a and b.
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swapping a is: ",a)
print("Before swapping b is: ",b)
a,b=b,a
print("After swapping a is: ",a)
print("After swapping b is: ",b)