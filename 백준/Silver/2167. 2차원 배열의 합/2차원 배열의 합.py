n,m=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
k=int(input())
for _ in range(k):
    result=0
    i,j,x,y=map(int, input().split())
    for t in range(i, x+1):
        for h in range(j, y+1):
            result+=arr[t-1][h-1]
    print(result)