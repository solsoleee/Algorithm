n,m,k=map(int, input().split())
arr=list(map(int, input().split()))
res=0
arr.sort()

res+=(m//k) * k * arr[-1] #번만큼 더하기

res+=(m%k) * arr[-2]

print(res)