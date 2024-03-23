import heapq

n = int(input())

lectures = [tuple(map(int, input().split()) for _ in range(n))]
lectures.sort(key=lambda x: (x[0], x[1]))

rooms = []

for s, t in lectures:
    if rooms and rooms[0] <=s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, t)