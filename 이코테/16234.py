n,l,r = map(int, input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

res=0
while True:
    data=[] #연합 국가 위치
    for i in range(n):
        for j in range(n):
            if i+1 < n:
                if l <=abs(arr[i][j]-arr[i+1][j])<=r:
                    data.append((i,j))
                    data.append((i+1,j))

            if j+1 < n:
                if l <=abs(arr[i][j]-arr[i][j+1])<=r:
                    data.append((i,j))
                    data.append((i,j+1))

    data=set(data)
    count=len(data)

    if count == 0:
        break

    people=0
    for x,y in data:
        people+=arr[x][y]
    
    divide=int(people//count)
    
    for x, y in data:
        arr[x][y]=divide
    res+=1
print(res)

