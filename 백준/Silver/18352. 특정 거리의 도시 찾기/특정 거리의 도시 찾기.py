from collections import deque

n,m,k,x=map(int, input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)

distance=[-1]*(n+1)
distance[x]=0
def bfs(v):
    que=deque([v])
    while que:
        now=que.popleft()
        for i in graph[now]:
            if distance[i]==-1:
                distance[i]=distance[now]+1
                que.append(i)
bfs(x)

check=False
for i in range(1, len(distance)):
    if k==distance[i]:
        print(i)
        check=True

if not check:
    print(-1)