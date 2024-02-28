n,m=map(int, input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

result=1
for i in arr:
    print(min(i))
    result=max(result, min(i))

print(result)