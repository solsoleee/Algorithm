n,k=map(int, input().split())

arr=[0]

for i in range(n):
    w,v=map(int, input().split())
    arr.append((w,v))


arr.sort(key=lambda x: x[0])

print(arr)

start=0
end=len(arr)


result=0

while start <=end:
    mid=(start+end)//2
    for i in range(mid):
        result=result+arr[i][0]
    if result < k:
        start=mid+1
    else:
        end=mid-1

print(result)