from collections import deque

n,m,v=map(int, input().split())

graph=[[0]*(n+1)for _ in range(n+1)]
visited1=[0]*(n+1)
visited2=[0]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

def dfs(v):
    visited1[v]=1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited1[i]==0 and graph[v][i]==1:
            dfs(i)

def bfs(v):
    que=deque([v])
    visited2[v]=1
    while que:
        v=que.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i]==0 and graph[v][i]==1:
                que.append(i)
                visited2[i]=1
dfs(v)
print()
bfs(v)