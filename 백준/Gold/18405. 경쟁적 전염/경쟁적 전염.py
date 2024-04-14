from collections import deque
n,k=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

s,a,b=map(int, input().split())

second=0
data=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            data.append((arr[i][j], i, j, second))
data.sort() #우선순위 정렬
que=deque(data)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

while que:
    virus, x, y, second = que.popleft()
    if s==second:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
            arr[nx][ny] = virus
            que.append((virus, nx, ny, second+1))

print(arr[a-1][b-1])