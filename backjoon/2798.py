result=0
a,b=map(int,input().split())
n=list(map(int,input().split()))
for i in range(a):
    for j in range (i+1,a):
        for k in range(j+1,a):
            sum=n[i]+n[j]+n[k]
            if sum<=b:
                result=max(result,sum)
print(result)