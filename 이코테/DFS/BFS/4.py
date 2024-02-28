from collections import deque

n,m=map(int, input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==1:
                    print(nx, ny)
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))

print(graph[n-1][m-1])