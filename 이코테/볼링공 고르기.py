from itertools import combinations

n,m=map(int, input().split())

bowling=list(map(int, input().split()))
res=[]
for a,b in combinations(bowling, 2):
    if a!=b:
        res.append((a,b))

print(len(res))


# count = [0] * (m+1)
# for ball in balls:
#     count[ball] += 1

# for i in range(1, m+1):
#     n-=count[i]
#     result+=count[i] * n