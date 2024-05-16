n=int(input())
arr=[]
for i in range(n):
    arr.append(list(input().split()))
    for j in range(1,4):
        arr[i][j]=int(arr[i][j])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])