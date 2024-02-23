from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def bfs():
        answer = 0
        que=deque()
        que.append((begin, 0))
    
        while que:
            w, step =que.popleft()
            if w==target:
                return step
            for i in words:
                cnt=0
                for j in range(len(w)):
                    if w[j]!=i[j]:
                        cnt+=1
                if cnt==1:
                    que.append((i, step+1))      
    answer = bfs()
    
    return answer