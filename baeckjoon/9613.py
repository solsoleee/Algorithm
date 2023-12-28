import math

t=int(input())

for i in range(t):
    total=0 
    arr=list(map(int,input().split()))
    
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            total+=math.gcd(arr[j], arr[k])
    print(total)
    
    