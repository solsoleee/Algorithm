n=int(input())

dp=[]

for i in range(n):
    dp.append(list(map(int, input().split())))

#1번집
#2번집
#3번집 일 때..

for i in range(1,n): 
    #1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기 때문이다.
    dp[i][0]+=min(dp[i-1][1],dp[i-1][2]) #이번이 빨간색이라면 이전의 값은 다른 값
    dp[i][1]+=min(dp[i-1][0],dp[i-1][2])
    dp[i][2]+=min(dp[i-1][0],dp[i-1][1])


print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

# dp는 각 색상에 대하여 누적 최소값을 나타낸다
# 첫번째의 값은 각각 빨간색, 초, 파 첫번째 값을 넣어준다
# 두 번째 값부터는 집이 연속된 색상을 가지지 말아야한다
