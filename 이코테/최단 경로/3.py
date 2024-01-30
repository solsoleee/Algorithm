import heapq
n,m,c =map(int, input().split())

graph=[[] for _ in range(n+1)]

INF=int(1e9)
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z))

print(graph)

def dijkstra(c):
    q=[]
    distance[c]=0
    heapq.heappush(q,(0,c))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #지금 거리가 더 작으면 업데이트 필요 없음
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
                
dijkstra(c)

cnt=0
time=0
for d in distance:
    if d!=INF:
        cnt+=1
        time=max(d, time)

print(cnt-1, time)