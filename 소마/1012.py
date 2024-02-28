def dfs(x,y):
    graph[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            return False
        else:
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                dfs(nx,ny)
    return False

t=int(input())

for _ in range(t):

    m,n,k=map(int, input().split())

    graph=[[0]*m for _ in range(n)]

    for i in range(k):
        x,y=map(int, input().split())
        graph[y][x]=1

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    result=0

    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                if dfs(i,j):
                    graph[i][j]=0
                    result+=1

    print(result)
