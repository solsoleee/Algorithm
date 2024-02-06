
n,k=map(int, input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
print(arr)

print(arr[0])









