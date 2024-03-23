import heapq
n=int(input())
time=[list(map(int, input().split())) for _ in range(n)]
print(time)

def solution(time):
    answer=[]
    
    time.sort(lambda x: (x[0], x[1]))
    print(time[0][1])
    print("aa")
    heapq.heappush(answer, time[0][1]) #처음에 넣어줌
    print(answer)
    for i in range(1, len(time)):
        if time[i][0] >= answer[0]:
            heapq.heappop(answer)
        heapq.heappush(answer[i][1])
    
    # print(answer)
    
    return answer