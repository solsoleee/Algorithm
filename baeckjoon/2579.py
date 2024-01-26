n=int(input())
d=[0]*301
arr=[0]*301
for i in range(1,n+1):
    arr[i]=int(input())
    
d[1]=arr[1]
d[2]=arr[1]+arr[2]
d[3]=max(arr[1]+arr[3], arr[2]+arr[3])

for i in range(4, n+1):
    d[i]=max(d[i-3]+arr[i-1]+arr[i],d[i-2]+arr[i])

print(d[n])