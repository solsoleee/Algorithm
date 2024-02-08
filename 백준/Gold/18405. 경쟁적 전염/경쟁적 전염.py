from collections import deque

n,k=map(int, input().split())

graph=[]
data=[]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j], 0, i, j)) #바이러스 번호, 시간, 인덱스

data.sort()
q=deque(data)

target_s,target_x,target_y=map(int, input().split())

dx=[1,0,-1,0]
dy=[0,1,0,-1]


def bfs():
    while q:
        target, s, x, y =q.popleft()
        if target_s==s:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=target
                    q.append((target, s+1, nx, ny))
    return

bfs()
print(graph[target_x-1][target_y-1])