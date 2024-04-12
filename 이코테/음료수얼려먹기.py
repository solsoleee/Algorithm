from collections import deque

n,m=map(int, input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int, input())))


def bfs(x,y):

    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
                que.append((nx,ny))
                arr[nx][ny]=1
    return True

cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            if bfs(i,j):
                cnt+=1
        
     
print(cnt)


# def dfs(x,y):
#     if x-1>=0 and y-1>=0 and x+1<n and y+1<m and arr[x][y]==0:
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x,y-1)
#         arr[x][y]=1
#         return True
#     return False
        

# cnt=0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j):
#             cnt+=1

# print(cnt)