import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    x,y=map(int, sys.stdin.readline().split())
    arr.append((x,y))

arr.sort(key=lambda x:(x[1],x[0]))

cnt=1
end_time=arr[0][1]

for i in range(1, n):  
    if arr[i][0] >= end_time:
        cnt+=1
        end_time=arr[i][1]
print(cnt)
