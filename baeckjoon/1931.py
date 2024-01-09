N=int(input())

d=[[0] * (2) for _ in range(N)]

for i in range(N):
    a,b=map(int, input().split())
    d[i][0]=a
    d[i][1]=b

d.sort(key=lambda x: (x[1], x[0]))

print(d)