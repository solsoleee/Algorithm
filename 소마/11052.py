n=int(input())

p=[0]+list(map(int, input().split()))

dp=[0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i]=max(dp[i], dp[i-j]+p[j])

print(dp[n])

#가치의 합이 k원이 되는 경우의 수를 구하는 전체의 문제를
#가치의 합이 i원이 되는 경우의 수를 구하는 부분
#특정 동전을 썼을 때 가치의 합이 i원이 되는 경우의 수

