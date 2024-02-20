from collections import deque

def solution(n, computers):
    visited=[0]*(n+1)
    def bfs(v, visited) :
        que=deque([v])
        visited[v]=1
        while que:
            v=que.popleft()
            for i in range(n):
                if visited[i]==0 and computers[v][i]==1:
                    que.append(i)
                    visited[i]=1
        
        return False
    answer = 0
    for i in range(n):
        for j in range(n):
            if visited[j]==0 and computers[i][j]==1:
                bfs(j, visited)
                answer+=1
    
    return answer