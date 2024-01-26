import heapq
import sys
iuput=sys.stdin.readline
INF=int(1e9)

n,m=map(int, input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[] #우선 순위 큐
    heapq.heappush(q, (0, start)) #첫번째 우선 순위, 노드 숫자
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist:  #0,1 
            continue
        for i in graph[now]: #1이랑 이어진 리스트 확인
            cost=dist+i[1] # 현재 거리에서 + 이어진 리스트의 거리 더하기
            
            if cost < distance[i[0]]: 
                distance[i[0]] = cost #거리 테이블 업데이트
                heapq.heappush(q(cost, i[0])) #heap도 업데이트

dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])