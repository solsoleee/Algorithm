#최단거리니까 bfs로 구현해야지..
#distance table를 만들어서 현재 거리에서 다른 거리로 갈 때마다 +1을 더해주면 된다

from collections import deque

n,m,k,x=map(int,input().split())

graph=[[]*(m+1)for i in range(n+1)]
distance=[-1]*(n+1)
for i in range(1, m+1):
    a,b=map(int, input().split())
    graph[a].append(b)

def bfs(x):
    q=[]
    q=deque([x])
    distance[x]=0
    while q:
        x=q.popleft()
        for node in graph[x]:
            if distance[node]==-1:
                distance[node]=distance[x]+1
                q.append(node)
bfs(x)
check=False

for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check=True
if not check:
    print(-1)

