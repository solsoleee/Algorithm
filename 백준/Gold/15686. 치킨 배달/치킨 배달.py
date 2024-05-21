from itertools import combinations

n,m = map(int, input().split())

arr=[]

for _ in range(n):
        arr.append(list(map(int, input().split())))

home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        if arr[i][j] == 2:
            chicken.append((i,j))

selected_chicken=list(combinations(chicken, m))
answer = 1e9
for selected in selected_chicken:
    res = 0
    for r1, c1 in home:
        distance = 1e9
        for r2, c2 in selected:
            ans = abs(r1-r2) + abs(c1-c2)
            distance = min(ans, distance)
        res += distance
    answer = min(res, answer)

print(answer)
