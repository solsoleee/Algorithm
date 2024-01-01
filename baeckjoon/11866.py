import sys

N, K = map(int, sys.stdin.readline().split())

arr=[i for i in range(1, N+1)]

cycle=[]
cnt=0
for i in range(N):
    cnt+=K-1
    if cnt>len(arr):
        cnt=cnt%len(arr)
        cycle.append(arr.pop(cnt))
    else:
        cycle.append(arr.pop(cnt))
        
print("<",', '.join(str(cycle)),">",sep="")