n=int(input())
k=int(input())

arr=[[0]*(n+1) for i in range(n+1)]

result=[]
for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j]=i*j
        result.append(i*j)

result.sort()
print(result[k])