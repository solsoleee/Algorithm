from collections import deque

n,m=map(int, input().split())
arr=deque()
for i in range(n):
    arr.append(list(map(int, input())))
    
print(arr)