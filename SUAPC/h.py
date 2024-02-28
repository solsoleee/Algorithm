import sys

n=int(sys.stdin.readline())

arr=[[] for i in range(n+1)]

for i in range(1, n+1):
    arr[i].append(sys.stdin.readline().rstrip())


for j in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a][0]=arr[a][0]+arr[b][0]
    arr[b][0]=''

for k in arr:
    if k and k[0]!='':
        print(k[0])
        

# n = int(input())

# # 각 노드의 값을 리스트로 저장
# arr = [[] for _ in range(n + 1)]

# for i in range(1, n + 1):
#     arr[i].append(input())

# # Union-Find 알고리즘을 위한 부모 노드 정보 초기화
# parent = [i for i in range(n + 1)]

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(x, y):
#     x_root = find(x)
#     y_root = find(y)
#     if x_root != y_root:
#         parent[y_root] = x_root
        
#         arr[x_root].extend(arr[y_root])
#         arr[y_root] = []


# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     union(a, b)


# for k in arr:
#     if k:
#         print(''.join(k))
