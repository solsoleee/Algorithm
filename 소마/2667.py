from collections import deque

n=int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# def bfs(x,y):
#     global cnt
#     que=deque()
#     que.append((x,y))
#     arr[x][y]=0
#     cnt=1
#     while que:
#         x,y=que.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx>=0 and nx<n and ny>=0 and ny<n:
#                 if arr[nx][ny]==1:
#                     que.append((nx,ny))
#                     arr[nx][ny]=0
#                     cnt+=1
#     return cnt



def dfs(x,y):
    if x-1<0 or x>=n or y-1<0 or y>=n:
        return False
    if arr[x][y]==1:
        arr[x][y]=0
        cnt+=1
        dfs(x-1,y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
dfs(1,1)
        
            
# res=[]
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==1:
#             res.append(bfs(i,j))

# res.sort()
# print(len(res))
# for i in res:
#     print(i)
