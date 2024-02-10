n,m=map(int, input().split())

graph=[]
temp=[[0]*(m) for i in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

#2로 퍼뜨림
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)
#0의 개수를 세워줌
def get_sum():
    total=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                total+=1
    return total

res=0

#완전 탐색으로 3개 벽을 세우고 0을 하나씩 확인함
def dfs(count):
    global res
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        
        res=max(get_sum(), res)
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0
                count-=1
dfs(0)            
print(res)