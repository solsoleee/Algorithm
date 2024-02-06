from collections import deque
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input())))

print(arr)
dx=[1, -1, 0, 0]
dy=[0,0,-1,1]

def bfs(x,y):
    global res
    res=0
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>n or ny>n:
                continue
            if arr[nx][ny]==1:
                res+=1
                que.append((nx,ny))
    return res

print(bfs(1,1))
# def dfs(x,y):
#     arr[x][y]=0
#     for i in range(n+1):

#         if x-1<0 or y-1<0 or x>n or y>n:
#             continue
#         if arr[x][y]==1:
#             dfs(x-1)
#             dfs(x+1)
#             dfs(y-1)
#             dfs(y+1)
#             arr[x][y]=0
#             return 1
        
# print(dfs(0,0))
