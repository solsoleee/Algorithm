import sys
sys.setrecursionlimit(10000)

t=int(sys.stdin.readline())
for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())

    arr=[[0]*(m) for _ in range(n)]

    for i in range(k):
        x,y=map(int,sys.stdin.readline().split())
        arr[y][x]=1

    def dfs(x,y):
        if x<0 or y<0 or x>=n or y>=m:
            return False
        if arr[x][y]==1:
            arr[x][y]=0
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
        return False

    result=0

    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1

    print(result)

    

