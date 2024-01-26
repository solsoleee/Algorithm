n,m=map(int,input().split())

graph=[[0]*(n+1)for i in range(n+1)]
visited=[0]*(n+1)


for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
    
print(graph)

def dfs(v):
    visited[v]=1
    print(v, end=' ')
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]:
            dfs(i)
            visited[i]=1
            return True

result=0
dfs(1)
print()
dfs(2)
print()
dfs(3)
print()
dfs(4)
# for i in range(1,n+1):
#     if dfs(i)==True:
#         result+=1
# print(result)