from itertools import combinations

n,m=map(int, input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
#치킨집은 최대 m개를 남기고 없애야한다
#치킨집 조합을 뽑고 그 거리가 최소인것을 구하면 된다.

chicken=[]
home=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append((i,j))
        if graph[i][j]==1:
            home.append((i,j))
            
arr=list(combinations(chicken,m))

def get_sum(candidate):
    result=0
    for x,y in home:
        temp=1e9
        for i, j in candidate:
            temp=min(temp, abs(x-i)+abs(y-j))
        result+=temp
    return result

result=1e9
for c in arr:
    result=min(result, get_sum(c))

print(result)