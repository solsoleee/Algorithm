from collections import deque
n,m=map(int, input().split())

graph=[]
temp=[[0]*(m) for i in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
result=0

#2를 퍼지게 함
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

#점수를 계산함
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

#벽을 세우면서 0의 최댓값을 계신
def dfs(count):
    global result
    #울타리가 3개 설치된경우
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]
                
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result, get_score())
        return
    #울타리를 세움
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0
                count-=1
    
dfs(0)
print(result)
