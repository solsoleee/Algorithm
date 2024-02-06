n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
d=[0]*100001
d[1]=arr[0]
for j in range(1, n+1):
    d[i]+=d[i]+d[i-1]+arr[i-1]
    print(d[i])