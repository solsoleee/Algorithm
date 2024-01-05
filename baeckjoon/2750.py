N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr.sort()

print("\n".join(map(str, arr)))