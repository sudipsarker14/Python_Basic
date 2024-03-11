'''
l = []
while True:
    c = int(input(
                  1 Push Elements
                  2 Pop Elements
                  3 Peek Elements
                  4 Display Stack
                  5 Exit
                  ))
    
    if c==1:
        n = input("Enter The value:- ");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        l.pop()
        print(l)
    elif c==3:
        print("The 6peek element is ",l[-1])
    elif c==4:
        print(l)
    elif c==5:
        break
    else:
        print("Invalid chose")
'''

l = []
while True:
    c = int(input('''
                  1 Enqueue Elements
                  2 Dequeue Elements
                  3 front Elements
                  4 last Element
                  5 Display Queue
                  6 Exit
                  '''))
    
    if c==1:
        n = input("Enter The value:- ");
        l.append(n)
        print(l)
    elif c==2:
        del(l[0])
        print(l)
    elif c==3:
        print("The first element is ",l[0])
    elif c==4:
        print("The last element is ",l[-1])
    elif c==5:
        print(l)
    elif c==6:
        break
    else:
        print("Invalid chose")


