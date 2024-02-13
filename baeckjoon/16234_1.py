#bfs로 상하좌우 다 파악을 해서 count를 해준다
#sum도 구한다
#방문하지 않거나 연합인 국가가 아니면 반복해서 파악한다

from collections import deque

n,l,r=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))


dx=[1,0,-1,0]
dy=[0,1,0,-1]

#연합 국가 파악하고 sum이랑 count 구해줌
def bfs(x,y):
    united=[] #연합인 국가를 담는 리스트
    que=deque()
    que.append((x,y))
    united.append((x,y))

    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        que.append((nx, ny))
                        united.append((nx,ny))
    return united

res = 0
while True:
    visited=[[0]*(n) for _ in range(n)] #방문했는지 안했는지 파악
    flag=0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:  # 방문하지 않은 국가에 대해서만 BFS 호출
                visited[i][j]=1
                country=bfs(i, j)  # 연합을 이루는 국가가 있을 경우

                if len(country)>1:
                    flag=1
                    total=sum(graph[x][y] for x,y in country)//len(country)
                    
                    for x,y in country:
                        graph[x][y]=total
    if flag==0:
        print(res)
        break
    res+=1
    