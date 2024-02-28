s=int(input())

arr=[0]*301

for i in range(1,s+1):
    arr[i]=int(input())

d=[0]*301

d[1]=arr[1]
d[2]=arr[1]+arr[2]
d[3]=max(arr[1]+arr[3], arr[2]+arr[3])
for i in range(4, s+1):
    d[i]=max(arr[i]+d[i-2], arr[i]+d[i-3]+arr[i-1])

print(d[s])