from collections import deque
n,m,v=map(int, input().split())

graph=[[False]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a][b]=True
    graph[b][a]=True
    
def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for next in range(1, n+1):
        if not visited[next] and graph[v][next]:
            dfs(next)
            visited[next]=True

def bfs(v):
    que=deque([v])
    visited[v]=True
    while que:
        v=que.popleft()
        print(v, end=' ')
        for next in range(1, n+1):
            if not visited[next] and graph[v][next]:
                que.append(next)
                visited[next]=True

# dfs(v)
bfs(v)