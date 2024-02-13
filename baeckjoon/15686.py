n,m=map(int, input().split())

graph=[]
chicken=[]
home=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    

for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append((i,j))
        if graph[i][j]==1:
            home.append((i,j))


res=[]

for i,j in home:
    result=[]
    for x,y in chicken:
        result.append(abs(x-i)+abs(y-j))
    res.append(result)
    
print(res)

answer=[]
for j in res:
    answer.append((min(j), j.index(min(j))))


print(answer)