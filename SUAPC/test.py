def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, q = map(int, input().split())

edges = []
for _ in range(m):
    x, y, college = input().split()
    x, y = int(x), int(y)
    edges.append((1, x, y, college))  # 비용을 1로 설정하여 모든 간선을 동일하게 처리

parent = [i for i in range(n + 1)]
edges.sort()

college_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
for cost, x, y, college in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        college_count[college] += 1

for _ in range(q):
    a, b, c, d, e = map(int, input().split())
    total_cost = (a * college_count['A'] + b * college_count['B'] +
                  c * college_count['C'] + d * college_count['D'] +
                  e * college_count['E'])
    print(total_cost)
