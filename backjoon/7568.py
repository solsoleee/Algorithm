n=int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    if (a[i]<a[i+1] and b[i]<b[i+1]):
        rank=1