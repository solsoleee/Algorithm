from collections import deque
n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque((x,y))
    
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or n>=n or ny < 0 or ny>=n:
                continue
            
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                que.append((nx,ny))
    return graph[n-1][m-1]