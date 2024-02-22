from collections import deque

def solution(n, computers):
    answer = 0
    visited=[0]*(n+1)
    
    def bfs(x):
        que=deque([x])
        while que:
            x=que.popleft()
            visited[x]=1
            for i in range(n):
                if computers[x][i]==1 and visited[i]==0:
                    visited[i]=1
                    que.append(i)
                    print(i)
        return False
                    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 and visited[j]==0:
                bfs(j)
                answer+=1
            
        
    
    return answer