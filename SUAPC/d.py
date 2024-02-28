MOD = 998244353

def count_ways(N, A):
    counts = [0] * (N + 1)  
    zeros = A.count(0)  # 0의 개수

    # 0이 아닌 숫자의 등장 횟수 계산
    for num in A:
        if num > 0 and num <= N:
            counts[num] += 1
            if counts[num] > num: 
                return 0

    ways = 1
    for i in range(1, zeros + 1):
        options = 0  # i번째 0을 대체할 수 있는 숫자의 개수
        for num in range(1, N + 1):
            if counts[num] < num:
                options += 1
        ways = (ways * options) % MOD  # 가능한 경우의 수를 곱함
        if options > 0:
            counts[1] += 1  # 가장 작은 숫자를 하나 증가시킴

    return ways

# 입력
N = int(input())
A = list(map(int, input().split()))

# 결과 출력
print(count_ways(N, A))
