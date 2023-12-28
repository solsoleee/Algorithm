import sys

que=[]
N=int(sys.stdin.readline())
for i in range(N):
    command=input().split()
    if command[0]=="push":
        que.append(command[1])
    elif command[0]=="pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
        que.pop
    elif command[0]=="front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0]=="back":
        if que:
            print(que[-1])
        else:
            print(-1)
    elif command[0]=="size":
        print(len(que))
    else:
        if que:
            print(0)
        else:
            print(1)

    