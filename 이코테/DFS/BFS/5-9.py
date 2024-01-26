from collections import deque

def bfs(graph, start, visited):
    que=deque([start])
    visited[start]=True
    while que:
        v=que.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i]=True
                
