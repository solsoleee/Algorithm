#상, 하, 좌, 우를 본다음에 차이가 만족이 되면 다른 배열에 넣는다
# sum과 count를 계산해서 인구이동을 새로 넣어준다
# 만족할 때까지 반복한다 --> 나는 이 반복문이 생각나지 않았따.

from collections import deque
n,l,r=map(int, input().split())
graph=[]
temp=[[-1]*(n) for i in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

#특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def bfs(x,y, index):
    #x,y의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united=[]
    united.append((x,y))
    
    #너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    que=deque()
    que.append((x,y))
    union[x][y]=index #현재 연합의 번호 할당 !!!!!!!!!!!!!!!!!!!!!!!!!
    
    summary=graph[x][y] #현재 연합의 전체 인구 수
    count=1 #현재 연합의 국가 수
    
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if l<= abs(graph[x][y]-graph[nx][ny])<=r:
                    if temp[nx][ny]==-1:
                        que.append((nx,ny))
                        #연합에 추가
                        union[nx][ny]=index
                        summary+=graph[nx][ny]
                        count+=1
                        united.append((nx,ny))
    for i, j in united:
        graph[i][j]=summary//count
    return count

total_count=0

#새로 알게 된 사실, union에서 index값을 넣어주는거

while True:
    union=[[-1]*n for _ in range()]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1: #왜 union이라는 것을 설정했나면 이 나라가 연합인지 아닌지 방문 했는지 파악해주기 위해서이다
                bfs(i,j,index)
                index+=1
                
    if index==n*n:
        break
    total_count+=1
                