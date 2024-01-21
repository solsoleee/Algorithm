from collections import deque

# T=int(input())
# for i in range(T):
#     rank=1
#     n,m=map(int, input().split())
#     arr=map(int.input().split())
m=1
arr=[1,2,3,4]
rank=1
target=arr[0]
while arr:
    if arr[0] < max(arr):
        arr.append(arr.pop(0))
    else:
        print(arr.pop(0))
        rank+=1
    print(arr)