import heapq

def solution(food_times, k):
    
    # 구조= 최소힙을 사용하여 먼저 반환한다.. 우선 순위 큐를 사용..
    # 작은거에서 현재 길이를 곱해서 k보다 작은지 판단한다
    # k보다 작을 때까지 반복하고 그 배열에서 가르키는 수를 반환한다
    
    #예외처리 -1
    if sum(food_times) <=k:
        return -1
    
    #힙 구현
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    #현재 길이
    length=len(food_times)
    #먹은 총합
    sum_food=0
    #이전의 값
    previous=0
    
    while sum_food + (q[0][0]-previous)*length <=k:
        now=heapq.heappop(q)[0]
        sum_food+=(now-previous)*length
        length-=1
        previous=now
    
    result=sorted(q, key=lambda x: x[1])
    answer=result[(k-sum_food)%length][1]
    
    return answer

print(solution([3,1,2], 5))