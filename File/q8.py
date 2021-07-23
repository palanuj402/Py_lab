#Write a python program to find sum and average of elements in list
size=int(input("Enter size of list: "))
l1=[]
print("Enter elements: ")
for i in range(size):
    item=int(input())
    l1.append(item)


print("List is: ",l1)
#to find sum 
sum=0
for i in range(size):
    sum=sum+l1[i]
    # size=size-1

print("Sum is: ",sum)    

avg=float(sum/(size))
print("Average is: ",avg)