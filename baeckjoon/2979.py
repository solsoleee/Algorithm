a,b,c=map(int, input().split())
cnt=[0]*100

for i in range(3):
    n,m=map(int, input().split())
    for j in range(n, m):
        cnt[j]+=1

result=0

for k in cnt:
    if k==1:
        result+=a*k
    elif k==2:
        result+=b*k
    elif k==3:
        result+=c*k

print(result)