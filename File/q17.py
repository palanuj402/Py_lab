#  Write a python program to implement stack (Push, Pop, Display, Peek Operations)
stack=[]
size=int(input("Enter size of stack: "))
#menu
while True:
    print('1.push ')
    print('2.pop')
    print("3.Display")
    print("4.Peek")
    ch = int(input('Enter your choice: '))

    if(ch==1):
        if(len(stack)==size):
            print("Overflow Conditon")
            break
        val=int(input("Enter a value to br pushed: "))
        stack.append(val)
        print(val," is pushed to stack ")
        
    elif(ch==2):
        if(len(stack)==0):
            print("Underflow condition")
            break
        stack.pop()
        print("Last element is Popped")
        
    elif(ch==3):
        if (stack==[]):
            print("Stack is empty ")
            break
        print("Stack is: ")
        for i in range(len(stack)):
            print(stack[i],end=" ")
        print()
        
    elif(ch==4):
        print("TOP ele is: ",stack.top())
        
           