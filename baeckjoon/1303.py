from collections import deque

n,m=map(int, input().split())

arr=[list(input()) for _ in range(m)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y,N): #x,y 축
    cnt=0
    que=deque()
    que.append((x,y))
    arr[x][y]=0
    while que:
        x,y=que.popleft()
        cnt+=1    
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<m) and (0<=ny<n) and arr[nx][ny]!=0:
                if arr[nx][ny]==N:
                    que.append((nx,ny))
                    arr[nx][ny]=0
    return cnt

w_sum=0
b_sum=0

for i in range(m):
    for j in range(n):
        if arr[i][j]=='W':
            w_sum+=bfs(i,j,'W')**2
        elif arr[i][j]=='B':
            b_sum+=bfs(i,j,'B')**2
print (w_sum,b_sum)