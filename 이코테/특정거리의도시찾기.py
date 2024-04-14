from collections import deque

n,m,k,x=map(int, input().split())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)


que=deque()
que.append(x)
while que:
    x=que.popleft()
    for next_node in graph[x]:
        if visited[next_node]==0: #방문하지 않았다면
            visited[next_node]=visited[x]+1
            que.append(next_node)
# check=False
# for i in range(n+1):
#     if k==visited[i]:
#         print(i)
#         check=True

result=[i for i, v in enumerate(visited) if v==k]
if result:
    for r in result:
        print(r)
else:
    print("-1")
# print(result)

# if not check:
#     print("-1")