n=int(input())
graph=[[0]*n for _ in range(n)]

k=int(input())
for i in range(k):
    a,b=map(int, input().split())
    graph[a-1][b-1]=1

command=[]
l=int(input())
for i in range(l):
    a,b=input().split()
    command.append((int(a), b))

print(command)

#방향 전환하는 함수
#벽에 닿거나 자기 자신과 붙이치는 경우