



def solution(n):
    
    mid=1000000007
    
    if n%2!=0:
        return 0
    
    dp=[0]*(n+1)
    dp[2]=3
    dp[4]=11
    
    for i in range(6, n+1, 2):
        dp[i]=dp[i-2]*3 +2
        for j in range(i-4, -1, -2):
            dp[i]+=dp[j]*2
    
    dp[n]=dp[n]%mid
    return dp[n]

print(solution(6))
    
    