#dfs

from collections import deque

N,M,V = map(int, input().split())

arr=[[False] * (N+1) for _ in range(N+1) ]


for i in range(M):
    a,b=map(int, input().split())
    arr[a][b]=True
    arr[b][a]=True

visited1=[False]*(N+1)
visited2=[False]*(N+1)

def dfs(V):
    visited1[V] = True
    print(V,end=" ")
    for i in range(1, N+1):
        if not visited1[i] and arr[V][i]:
            dfs(i)


def bfs(V):
    q=deque([V])
    visited2[V]=True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited2[i] and arr[V][i]:
                q.append(i)
                visited2[i]=True

dfs(V)
print()
bfs(V)