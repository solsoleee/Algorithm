from itertools import combinations

def solution(n, s, arr):
    answer = 0
    
    for i in range(1, n+1):  # n을 포함하도록 범위를 조정합니다.
        for x in combinations(arr, i):
            if sum(x) == s:
                answer += 1

    return answer

n, s = map(int, input().split())  # n과 s를 입력받습니다.
arr = list(map(int, input().split()))  # arr에 대한 입력을 받습니다.

print(solution(n, s, arr))  # 수정된 함수 호출 방식
