from collections import deque

n,m=map(int, input().split())

arr=[]
for _ in range(n):
    arr.append(list(map(int, input())))

def bfs(x,y):
    global cnt
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if arr[nx][ny]==1:
                    arr[nx][ny]=arr[x][y]+1
                    que.append((nx,ny))
                    

bfs(0,0)

print(arr[n-1][m-1])