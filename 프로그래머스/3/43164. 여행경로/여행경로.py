from collections import deque
def solution(tickets):
    answer = []
    
    
    def bfs(tickets):
        que=deque()
        que.append(("ICN",["ICN"],[]))
        
        while que:
            now, path, index=que.popleft()
            if len(index)==len(tickets):
                answer.append(path)
                
            for i, ticket in enumerate(tickets):
                if ticket[0]==now and not i in index:
                    que.append((ticket[1], path+[ticket[1]], index+[i]))
        
    bfs(tickets)
    answer.sort()
    return answer[0]