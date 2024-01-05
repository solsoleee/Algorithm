K,N=map(int,input().split())

arr=[]
for i in range(K):
    x=int(input())
    arr.append(x)
    
start=1
end=max(arr)

result=0
while start <= end:
    cnt=0
    mid=(start+end)//2
    for i in arr:
        cnt+=i//mid
    if cnt < N: # 더 작은 값으로 잘라야함
        end=mid-1
    else:
        result=mid
        start=mid+1
        
print(result)