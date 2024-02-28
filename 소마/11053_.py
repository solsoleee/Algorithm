def solution(n, A):
    answer=0
    
    dp=[1]*(n)
    
    for i in range(1,n):
        for j in range(i):
            if A[i]>A[j]:
                dp[i]=max(dp[i],dp[j]+1)
    print(dp)
        
    return answer


solution(6, [10, 20, 10, 30, 20, 50])