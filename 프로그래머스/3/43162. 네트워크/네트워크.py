from collections import deque
def solution(n, computers):
    answer = 0
    
    
    visited=[0]*(n)
    def bfs(start):
        que=deque([start])
        visited[start]=1
        while que:
            now=que.popleft()
            for i in range(n):
                if visited[i]==0 and computers[now][i]==1:
                    que.append(i)
                    visited[i]=1
                    
    for i in range(n):
        for j in range(n):
            if visited[j]==0 and computers[i][j]==1:
                bfs(j)
                answer+=1
        
    return answer