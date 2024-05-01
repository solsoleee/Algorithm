N=int(input())

N, M = map(int, input().split())

arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

res=0
for i in range(N-M-1):
    for j in range(N-M-1):
        for k in range(M):
            arr[i][j]+arr