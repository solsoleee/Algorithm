from collections import deque

n,m=map(int, input().split())
graph=[]
dx=[1, -1, 0, 0] #상하좌우
dy=[0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))
    
def bfs(x,y):
    que=deque()
    for i in range(4):
        x=dx[i]
        y=dy[i]
        que.append(x,y)
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if arr[x][y]==1:
        return True