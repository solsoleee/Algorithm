n=int(input())

arr=list(map(int, input().split()))

arr.reverse()

print(arr)

dp=[1]*(n+1)

for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i], dp[j]+1)