from collections import deque

n,k=map(int, input().split())

arr=[0]*100001

def bfs():
    que=deque()
    que.append(n)
    while que:
        x=que.popleft()
        if x==k:
            print(arr[x])
            break
        for nx in [x-1, x+1, x*2]:
            if nx>=0 and nx<100001 and arr[nx]==0:
                arr[nx]=arr[x]+1
                que.append(nx)

bfs()