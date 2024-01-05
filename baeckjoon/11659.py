import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
pre_sum = [0]

temp = 0
for i in arr:
    temp += i
    pre_sum.append(temp)

print(pre_sum)
        