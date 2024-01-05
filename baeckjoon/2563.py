import sys

N=int(sys.stdin.readline())

arr=[[0 for j in range(101)] for i in range(101)]

cnt=0

for i in range(N):
    a,b=map(int, sys.stdin.readline().split())

    for j in range(a, a+10):
        for k in range(b, b+10):
            arr[j][k]=1

for i in arr:
    cnt+=i.count(1)

print(cnt)