n=int(input())
cnt=0
if n>=5:
    cnt+=n//5
    n=n%5
    print(cnt)
    print(n)
if n>=2:
    cnt+=n//2
    n=n%2

print(cnt)