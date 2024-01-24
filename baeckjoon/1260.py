from collections import deque
n,m,v=map(int, input().split())

graph=[[False] * (n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=True
    graph[y][x]=True

def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)
            
def bfs(v):
    que=deque([v])
    visited[v]=True
    while que:
        v=que.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited[i] and graph[v][i]:
                que.append(i)
                visited[i] = True

# dfs(v)
bfs(v)