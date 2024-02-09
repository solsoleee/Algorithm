from collections import deque
n=int(input())
graph=[]
new_graph=[]
res=[]


for i in range(n):
    graph.append(list(input().split()))
    
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def virus(count):
    if count==3:
        for i in range(n):
            for j in range(n):
                new_graph[i][j]=graph[i][j]

def bfs(x,y):
    q=[]
    q=deque((x,y))
    while q:
        x,y=q.popleft()
        if new_graph[x][y]=='T':
            for i in range(n):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and nx<0 and ny<0:
                    if graph[nx][ny]=='O':
                        pass
                    if graph[nx][ny]=='S':
                        res.append('NO')
                    if graph[nx][ny]=='X':
                        q.append((nx, ny))

    count=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='X':
                graph[i][j]='O'
                count+=1
                if count==3:
                    virus(count)
                    bfs(0,0)

print(graph)
print(new_graph)
            