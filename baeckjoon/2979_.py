a,b,c=map(int, input().split())

# 배열에 하나씩 cnt한다음에 나중에 더해주면 되겠다

cnt=[0]*101
result=0

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start,end):
        cnt[j]+=1

for k in cnt:
    if k ==0:
        pass
    elif k==1:
        result+=k*a
    elif k==2:
        result+=k*b
    else:
        result+=k*c

print(result)