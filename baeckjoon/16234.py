#그래프 각 상하좌우가 차이가 적합한지 확인
# 국경선이 열린거를 어떻게 표현할건지?
# 연합의 개수와 평균 확인

#위에 3과정이 계속 반복

#bfs를 써야겠따. 상하좌우..

from collections import deque
n,l,r=map(int, input().split())

graph=[]
visited=[[0]*(n+1) for i in range(n+1)]
res=[]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    
dx=[1, 0, -1,0]
dy=[0, 1, 0, -1]


def bfs(x,y):

    que=[]
    que=deque()
    que.append((x,y))
    global count, total
    count=1
    total=0
    total+=graph[x][y]
    visited[x][y]=1
    res.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if l<= abs(graph[x][y]-graph[nx][ny])<=r:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        count+=1
                        total+=graph[nx][ny]
                        que.append((nx,ny))
                        res.append((nx,ny))
                        print(res)
                        print(count, total)
bfs(0,0)

while res:
    x,y=res.pop()
    graph[x][y]=int(total/count)

print(graph)