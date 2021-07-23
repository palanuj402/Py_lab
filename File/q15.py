# Write a python program to generate a password.
import random

# val=random.random()
# val=random.randint(1,10)
# val=['A','B','C','D']
# val1=random.choice(val)
# print("Random num is : ",val1)

print("*****GENERATE PASSWORD*****")
l1=[]
word="abcdefghijklmnopqrstuvwxyz"
alpha2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in word:
    l1.append(i)
# print(l1)

l2=[]    
for i in alpha2:
    l2.append(i)
# print(l2)

l3=[]
word2="@#$%&*"
for i in word2:
    l3.append(i)
# print(l3)

l4=[]
word3="123456789"
for i in word3:
    l4.append(i)
# print(l4)

password=[]
v1=random.choice(l1)
v2=random.choice(l2)
v3=random.choice(l3)
v4=random.choice(l4)
password.append(v1)
password.append(v2)
password.append(v3)
password.append(v4)
print("Password is: ",password)