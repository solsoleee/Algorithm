n=int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

visited=[0]*(n+1)
sum_cost=0
INF = 1e8
ans=INF

def dfs(depth, x):
    global sum_cost, ans
    if depth==n-1:
        if cost[x][0]:
            sum_cost +=cost[x][0]
            if sum_cost < ans:
                ans = sum_cost
            sum_cost-=cost[x][0]
        return sum_cost
    
    for i in range(1,n):
        if visited[i]==0 and cost[x][i]:
            visited[i]=1
            sum_cost+=cost[x][i]
            dfs(depth+1, i)
            visited[i]=0
            sum_cost-=cost[x][i]

dfs(0,0)
print(ans)