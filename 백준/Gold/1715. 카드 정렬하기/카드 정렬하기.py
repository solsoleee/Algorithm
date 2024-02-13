#항상 가장 작은 크기의 두 카드 묶음을 꺼내서 이를 합친 뒤에 다시 리스트에 삽입하는 과정
# 우선순위 큐

import heapq
n=int(input())
heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap, data)

result=0

#힙에 원소가 1개 남을 때까지
while len(heap)!=1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    #카드 묶음을 합쳐서 다시 합침
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap, sum_value)

print(result)