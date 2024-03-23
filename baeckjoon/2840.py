import sys
input=sys.stdin.readline


#1. n으로 나누면 index를 신경쓸 필요가 없다.
#2. wheel[-s:] + wheel[:-s] s 단계만큼 시계 방향 회전 시키는 효과


def solution(n, record):
    wheel=["?"]*n #현재 바퀴
    for r in record:
        s =int(r[0])%n
        s_char=str(r[1])

        #큐가 아닌 리스트를 슬라이싱 한 후에 앞뒤 순서를 바꿔 다시 붙임
        wheel = wheel[-s:] + wheel[:-s]

        if wheel[0] == '?': #아무것도 없을 때
            if s_char in wheel: #지금 나온 문자가 있을 때
                return '!'
            wheel[0] = s_char
        elif wheel[0] == s_char: #같은게 나올 때
            continue
        else:
            return '!'
    else:
        return("".join(wheel))
        
        
n,k = map(int, input().split())
record = [input().split() for _ in range(k)]

print(solution(n, record))