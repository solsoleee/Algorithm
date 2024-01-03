N=int(input())
arr=[]
for i in range(N):
    arr.append(input())


arr=list(set(arr))

arr.sort(key=lambda x: len(x))
for j in arr:
    print(j)