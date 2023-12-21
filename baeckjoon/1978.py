N=int(input())
a=input().split()
count=0
for i in range(N):
    a[i]=int(a[i])
    cnt=0
    for j in range(1,1000):
        if(a[i]%j==0):
            cnt+=1
    if(cnt==2):
        count+=1
print(count)