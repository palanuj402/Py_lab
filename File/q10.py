#Write a python program to count occurrences of an element in a list.
size=int(input("Enter size of list: "))
l1=[]

for i in range(size):
    item=int(input())
    l1.append(item)

x=int(input("Enter element to find occurences: "))

count=0
for j in l1:
    if(j==x):
        count=count+1
print(x," has ",count," occurences")    
