from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for c in permutations(arr, m):
    print(*c)  # 튜플 `c`의 모든 요소를 공백으로 구분하여 출력합니다.