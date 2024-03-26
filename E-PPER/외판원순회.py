n=int(input())

cost=[list(map(int, input().split())) for _ in range(n)]

sum_value=0
ans=1e8
visited=[0]*(n+1) 

#최소비용, dfs, 백트래킹 이용
def dfs(depth, x):
    global sum_value
    global ans
    if depth == n-1:
        if cost[x][0]:
            sum_value+=cost[x][0]
            if sum_value < ans:
                ans = sum_value
            sum_value-=cost[x][0]
        
    for i in range(1, len(cost)):
        if visited[i]==0 and cost[x][i]:
            sum_value+=cost[x][i]
            visited[i]=1
            dfs(depth+1, i)
            sum_value-=cost[x][i]
            visited[i]=0


def solution(cost):
    dfs(0,0)
    return ans

print(solution(cost))