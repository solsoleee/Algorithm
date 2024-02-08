n,m=map(int, input().split())

graph=[] # 원래
new_graph=[[0]*m for i in range(n)] #벽을 세운 후

for i in range(n):
    graph.append(list(map(int, input().split())))

result=0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#2이면 퍼뜨리는 dfs
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if new_graph[nx][ny]==0:
                new_graph[nx][ny]=2
                virus(nx,ny)
            
#현재 맵에서 완전 영역의 크기 계산하는 메서드
def get_sum():
    total=0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j]==0:
                total+=1
    return total

#깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    if count==3:
        #count3이면 새로운 그래프에 벽을 세우고 바이러스 퍼져나감
        for i in range(n):
            for j in range(m):
                new_graph[i][j]=graph[i][j]
        for i in range(n):
            for j in range(m):
                if new_graph[i][j]==2:
                    virus(i,j)
        result=max(result, get_sum())
        return
    #완전 탐색으로 벽을 세움
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1 #벽을 3일 때까지 세움
                dfs(count) #그리고 3일 될때 result계산. 계산하고 나서 0으로 바꾸고 count-1해줌.
                graph[i][j]=0
                count-=1

dfs(0)
print(result)