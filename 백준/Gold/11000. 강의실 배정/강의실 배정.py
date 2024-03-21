import heapq


def solution(arr):
    answer=[]
    
    arr.sort(key=lambda x: (x[0], x[1]))
    
    heapq.heappush(answer, arr[0][1])

    for i in range(1, len(arr)):
        if answer[0] <= arr[i][0]:
            heapq.heappop(answer)
        heapq.heappush(answer, arr[i][1])        
    
    return len(answer)


n=int(input())

arr=[list(map(int, input().split())) for _ in range(n)]

print(solution(arr))
