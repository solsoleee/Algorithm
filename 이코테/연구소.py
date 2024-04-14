from collections import deque
from itertools import combinations

n,m = map(int, input().split())
graph=[] #원래 그래프
for _ in range(n):
    graph.append(list(map(int, input().split())))

new_graph=[[0]*m for _ in range(n)] #바이러스 계산 하는 위치

def virus(new_graph, x,y): #바이러스가 퍼져나감
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    que=deque()
    que.append((x,y))
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if new_graph[nx][ny]==0:
                    new_graph[nx][ny]=2
                    que.append((nx,ny))

def cnt(): #0의 개수를 셈
    zero_count=0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==0:
                zero_count+=1
    return zero_count

def dfs(count):
    count=0
    global result
    if count==3: #벽이 3개라면
        for i in range(n):
            for j in range(m): #바이러스
                    graph[i][j]=new_graph[i][j] #복사하는 과정
                    
        #바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if new_graph[i][j]==2:
                    virus(i,j)
        #값계산
        result=max(result, cnt())
        return 

    
    #벽을 세우는거
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0: 
                graph[i][j]=1 #벽을 세움
                count+=1
                dfs(count) #호춯
                graph[i][j]=0
                count-=1 

dfs(0)
print(result)