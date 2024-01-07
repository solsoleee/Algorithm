N=int(input())

arr = [[0] * (2) for i in range(N)]

for i in range(N):
    a,b=map(int,input().split())
    arr[i][0]=a
    arr[i][1]=b

arr.sort(key=lambda x:(x[1], x[0]))

cnt=1
end_time=arr[0][1]
print(arr)
print(arr[1][0])