#동적 계획법
#전체의 문제를 부분 문제로 잘 나누었는가? 그렇다면 전체 문제를 해결하기 위한 부분
#문제의 점화식은 무엇인가?

#부분 문제들을 해결하며 얻는 결과값을 메모리제이션하는가?
#부분 문제의 점화식은 부분 문제들 사이의 관계를 빠짐없이 고려하는가?


n,k=map(int, input().split())

coins=[]

d=[0]*(k+1)

for _ in range(n):
    coins.append(int(input()))

d[0]=1

for c in coins:
    for i in range(c,k+1):
        d[i]+=d[i-c]

print(d[k])