n=int(input())

arr=[]
res=0
visited=[]
for i in range(n):
    x,y=map(int, input().split())
    arr.append((x,y))

for x, y in arr:
    for i in range(x,x+10):
        for j in range(y,y+10):
            if not (i,j) in visited:
                res+=1
                visited.append((i,j))

print(res)