N, K = map(int, input().split())

arr=[i for i in range(1, N+1)]
num=0
result=[]

for i in range(N):
    if num+(K-1) >= len(arr):
        num=num%K
        result.append(arr[num+(K-1)])
    else:
        result.append(arr[num+(K-1)])
        num=num+K
    
print(*result)