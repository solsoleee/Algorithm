n=int(input())
m=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

print(graph)

def dfs(v):
    visited[v]=1
    for next in range(1,n+1):
        if visited[next]==0 and graph[v][next]:
            dfs(next)
            visited[next]=1

dfs(1)
print(sum(visited)-1)