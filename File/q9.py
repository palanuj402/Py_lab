#Write a python program take a list with both negative and
#positive numbers and separate them in two different lists.
size=int(input("Enter size of list: "))
l1=[]       #for all numbers 
l2=[]       #for +ve numbers
l3=[]       #for -ve numbers

for i in range(size):
    print("Enter element at index:",i)
    item=int(input())
    l1.append(item)

#checking +ve and -ve
for j in range(size):
    if(l1[j]>=0):
        l2.append(l1[j])
    else:
        l3.append(l1[j])    

print("Positive list : ",l2)
print("Negaitve list ",l3)  