#WAP to find largest and smallest in the list
l=[]
size=int(input("Enter size of list: "))
print("Enter elements: ")
for i in range (size):
    item=int(input())
    l.append(item)

print("List is: ")
for i in range (size):
    print(l[i],end=" ")
print()
# min=l[0]
# for i in range (size):
#     if min > l[i]:
#         min=l[i]

print("MIN in list is: ",min(l))        

# max=l[0]
# for i in range (size):
#     if max < l[i]:
#         max=l[i]

print("MAX in list is: ",max(l))
