from collections import deque

def solution(numbers, target):
    answer = 0
    
    #bfs를 이용해줄거임, 현재 합이랑, 현재 인덱스를 넣어줌
    que=deque()
    que.append((0,0))
    while que:
        current_sum, index = que.popleft()
        if index==len(numbers):
            for a,b in que:
                if a==target:
                    answer+=1
            print(answer)
            break
        que.append((current_sum+numbers[index], index+1))
        que.append((current_sum-numbers[index], index+1))


    return answer