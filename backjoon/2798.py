sum=0
a,b=map(int,input().split())
n=list(input().split())
for i in range(a):
    n[i]=int(n[i])
    sum+=n[i]
    if sum>=b:
        break
print(sum)