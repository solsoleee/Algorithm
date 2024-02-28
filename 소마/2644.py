from collections import deque

n=int(input())
a,b=map(int, input().split())

graph=[[0]*(n+1) for i in range(n+1)]


m=int(input())
for i in range(m):
    x,y=map(int, input().split())
    graph[x][y]=1
    graph[y][x]=1

visited=[0]*(n+1)

def bfs(start, target):
    que=deque()
    que.append((start, 0))
    visited[start]=1
    while que:
        x, index=que.popleft()
        if target==x:
            return index
        for i in range(1, n+1):
            if visited[i]==0 and graph[x][i]==1:
                que.append((i, index+1))
                visited[i]=1
    return -1

print(bfs(a,b))


