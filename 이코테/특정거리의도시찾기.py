from collections import deque

n,m,k,x=map(int, input().split())

arr=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1

que=deque()
que.append(x)
flag=False
cnt=0
while que:
    x=que.popleft()
    cnt+=1
    for i in range(n+1):
        if arr[x][i]==1:
            que.append(i)
            if cnt==k and visited[i]==0:
                for j in range(i,n+1):
                    if arr[x][j]==1 and visited[j]==0:
                        print(j)
                flag=True
                break
            visited[i]=1
if not flag:
    print("-1")

            