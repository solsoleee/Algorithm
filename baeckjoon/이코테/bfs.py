def dfs(x,y):
    cnt=0
    if x-1<0 or x>=n or y-1<0 or y>=m:
        return False

    if graph[x][y] ==1:
        cnt+=1
        graph[x][y] =0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print("sisi")
        return True
n,m=map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

result=0
for i in range(n):
    for j in range(m):
        
        if dfs(i,j):
            result+=1

