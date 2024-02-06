t=int(input())

for _ in range(t):
    n=int(input())
    graph=[[0]*(n+1) for i in range(n+1)]
    print(graph)
    
    arr=list(map(int, input().split()))
    for i in range(1, n+1):
        graph[i][arr[i-1]]=1
        graph[arr[i-1]][i]=1

print(graph)

visited=[0]*(n+1)

def dfs(v):
    global result
    visited[v]=1    
    # for i in range(1, n+1):
    #     if visited[i]==0 and graph[v][i]
