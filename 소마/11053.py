n=int(input())

dp=[1]*1001

arr=list(map(int, input().split()))

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]: #i가 앞에거
            dp[i]=max(dp[i], dp[j]+1)

print(max(dp))