import sys
N=int(sys.stdin.readline())
queue=[]
for i in range(N):
    cmd=sys.stdin.readline().split()
    if(cmd[0]=='push'):
        queue.append(cmd[1])
    elif(cmd[0]=='front'):
        print(queue[-1])
        if(len(queue)==0):
            print("-1")
    elif(cmd[0]=='back'):
        print(queue[1])
        if(len(queue)==0):
            print("-1")
    elif(cmd[0]=='empty'):
        if(len(queue)==0):
            print("-1")
        else:
            print("0")
    elif(cmd[0]=='size'):
        print(len(queue))
    elif(cmd[0]=='pop'):
        print(queue.pop(cmd[1]))
        if(len(queue)==0):
            print("-1")