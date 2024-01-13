n,k=map(int, input().split())
result=0
while n!=k:
    if n*2 < k:
        result+=1
        n=n*2
        print(n)
    elif n<k:
        n=n+1
        result+=1
    elif n>k:
        n=n-1
        result+=1

print(result)