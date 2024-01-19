N, M=map(int, input().split())

d=[-1]*10001

arr=[]
for i in range(N):
    arr.append(int(input()))

for k in range(2,M+1):    
    for j in arr:
        if k % j ==0:
            d[k]=d[k-j]+1
    

print(d[M])