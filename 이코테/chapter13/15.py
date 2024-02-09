#bfs로 풀어야지
#distance table을 이용해서 거리를 저장해야지
from collections import deque

n,m,k,x=map(int, input().split())
graph=[[] for i in range(n+1)]
distance=[-1]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)

distance[x]=0
#너비우선 탐색 수행
def bfs(x):
    que=deque([x])
    while que:
        now=que.popleft()
        for next_node in graph[now]: #현재 노드 중에서 연결된거
            if distance[next_node]==-1: #현재 방문하지 않은 도시
                distance[next_node]=distance[now]+1
                que.append(next_node)

bfs(x)
check=False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check=True
if not check:
    print(-1)
