from collections import deque

n,k=map(int, input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
x,y,s=map(int, input().split())

print(graph)

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# bfs 이용
# 1부터 s까지 반복

def bfs(x,y):
    l=0
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(n):                                             
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<n:
                    if graph[nx][ny]==0:
                        graph[nx][ny]=l
                        que.append((nx,ny))
    return graph


print(bfs(0,0))