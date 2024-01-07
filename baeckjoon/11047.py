N,K=map(int,input().split())

arr=[]
cnt=0
for i in range(N):
    arr.append(int(input()))    
arr.sort(reverse=True)

for j in arr:
    if j<=K: #같은것도 포함
        cnt+=K//j
        K=K%j
    if K==0:
        break
    
print(cnt)