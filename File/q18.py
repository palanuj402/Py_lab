#   Write a python program to implement queue (Enqueue, Dequeue, Display).
queue=[]

#menu
while True:
    print('1.Enqueue ')
    print('2.Dequue')
    print("3.Display")
    ch = int(input('Enter your choice: '))

    if(ch==1):
        val=int(input("Enter a value to enqueue: "))
        queue.insert(0,val)
    elif(ch==2):
        
        queue.pop()
        print("First element is Popped")    
    elif(ch==3):
        for i in range(len(queue)):
            print(queue[i],end=" ")
        print()        