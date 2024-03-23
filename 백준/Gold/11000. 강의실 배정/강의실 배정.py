import heapq
n=int(input())
time=[list(map(int, input().split())) for _ in range(n)]

def solution(time):
    answer=[]
    
    time.sort(key=lambda x: (x[0], x[1]))
    
    heapq.heappush(answer, time[0][1]) #처음에 넣어줌
    
    
    for i in range(1, len(time)):

        if time[i][0] >= answer[0]:
            heapq.heappop(answer)
        heapq.heappush(answer, time[i][1])
    
    return len(answer)

print(solution(time))