#Write a python program to check whether the given number is prime or not?
num=int(input("Enter a num to check prime or not: " ))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")