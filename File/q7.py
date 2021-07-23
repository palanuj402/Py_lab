# Write a program to print the multiplication table of a given number using for loop
a=int(input("Enter a num for printing table: "))

#using for loop
for i in range(1,11):
    print(a,"*",i,"=",a*i)