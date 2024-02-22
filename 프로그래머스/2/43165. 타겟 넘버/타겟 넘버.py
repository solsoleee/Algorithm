from collections import deque

def solution(numbers, target):
    
    def bfs(numsers, target):
        cnt=0
        now=[0] #모든 계산 결과
        for num in numbers: #numbers를 다 돌려줌
            tmp=[]
            for parent in now: #모든 계산 결과도 돌려줌
                tmp.append(parent+num) #현재 계산에서 새로운 값을 더하거나 뺀 것도 추가해줌
                tmp.append(parent-num)
            
            now=tmp #새로운 값으로 계속 update
        
        for n in now:
            if n==target:
                cnt+=1
        return cnt
    answer = bfs(numbers, target)
    return answer
        