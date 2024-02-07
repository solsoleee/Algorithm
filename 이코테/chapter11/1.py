n=int(input())

arr=list(map(int, input().split()))

arr.sort()

cnt=0
res=0

for i in arr:
    res+=1
    if res>=i:
        cnt+=1
        res=0
    
print(cnt)

