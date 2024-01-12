from collections import deque

n,m = map(int, input().split())

graph = [ ]

for i in range(n):
    graph.append(list(map(int, input().split()))
                 
                 

dx=[-1, 1, 0, 0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or n<0 ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
        return graph[n-1][m-1]
        
#상하좌우로 노드를 방문하면서..
#방문처리를 하고 
#bfs를 수행하려면,, 방문노드를 넣고, 그 노드에 인접해 있는 것들을 찾음
#dfs는 
#그니까 bfs는 pop할 때 그 인접한 노드들을 찾는거라면 dfs는 방문처리하고 재귀호출.. stack이니까 먼저 들어온게 먼저 나감.. 

dfs
