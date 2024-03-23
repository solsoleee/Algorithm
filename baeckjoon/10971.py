n=int(input())

arr=[list(map(int, input().split())) for _ in range(n)]
visited=[0]*(n+1)
sum_value=0
INF=1e8
ans=INF

def dfs(depth, x):
    global sum_value, ans
    if depth==n-1:
        if arr[x][0]:
            sum_value+=arr[x][0]
            if sum_value<ans:
                ans=sum_value
            sum_value-=arr[x][0]
        
    
    for i in range(1, n):
        if visited[i]==0 and arr[x][i]:
            sum_value+=arr[x][i]
            visited[i]=1
            dfs(depth+1, i)
            sum_value-=arr[x][i]
            visited[i]=0
            
dfs(0,0)
print(ans)