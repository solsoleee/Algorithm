import heapq

n=int(input())
card=[]
for _ in range(n):
    card.append(int(input()))

heapq.heapify(card)

answer=0

while len(card) > 1:
    first=heapq.heappop(card)
    second=heapq.heappop(card)
    sum_card=first+second
    answer+=sum_card
    heapq.heappush(card, sum_card)

print(answer)

