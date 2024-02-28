from collections import deque

def solution(n, wires):
    
    graph=[[0]*(n+1) for _ in range(n+1)]
    for x,y in wires:
        graph[x][y]=1
        graph[y][x]=1
    
    
    #연결된 bfs로 몇개 연결 되었는지 확인
    def bfs(start):
        visited=[0]*(n+1)
        cnt=1
        que=deque([start])
        visited[start]=1
        while que:
            v=que.popleft() #어디서 끊기는지
            # print(v)
            for i in range(1,n+1):
                if graph[v][i]==1 and visited[i]==0:
                    que.append(i)
                    visited[i]=1
                    cnt+=1
        return cnt
            
    # 완전 탐색으로 전력망 끊고 붙이면서 제일 적은거 확인해보기
    # for a,b in wires:
    # graph[1][3]=0
    # graph[3][1]=0
    # print(bfs(1))
    # print(bfs(3))
    res=[]
    for a,b in wires:
        graph[a][b]=0
        graph[b][a]=0
        
        res.append(abs(bfs(a)- bfs(b)))
        
        graph[a][b]=1
        graph[b][a]=1
    
    answer = min(res)
    return answer