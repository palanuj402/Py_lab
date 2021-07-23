#Number of rows 
R1=int(input("Enter Number of Rows for matrix 1: "))

#number of columns
C1=int(input("Enter number of columns for matrix 1: "))

#Number of rows 
R2=int(input("Enter Number of Rows for matrix 2: "))

# #number of columns
C2=int(input("Enter number of columns for matrix 2: "))

#initialyy matrix empty
matrix1=[]
matrix2=[]
sum_m= [[0,0,0],[0,0,0],[0,0,0]]

print("Enter numbers to Matrix 1: ")

#taking input for matrix 1
for i in range(R1):
    a=[]
    for j in range(C1):
        a.append(int(input()))
    matrix1.append(a)    

print("Enter numbers to Matrix 2: ")

#taking input for matrix 2
for i in range(R2):
    a=[]
    for j in range(C2):
        a.append(int(input()))
    matrix2.append(a)    

#dispaly matrix 1
print("matrix 1: ")
for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j],end=" ")
    print()    
# print(len(matrix1))

#dispaly matrix 2
print("matrix 2: ")
for i in range(R2):
    for j in range(C2):
        print(matrix2[i][j],end=" ")
    print()    
# print(len(matrix2))



#add
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        sum_m [i] [j] = matrix1 [i] [j] + matrix2 [i] [j]


print("Sum of matrix : ",sum_m)
