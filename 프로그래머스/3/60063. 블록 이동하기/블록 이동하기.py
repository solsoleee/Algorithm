from collections import deque

def solution(board):
    n = len(board)
    goal = (n-1, n-1)
    
    # 로봇의 초기 상태: ((첫 번째 칸 좌표), (두 번째 칸 좌표))
    start = ((0, 0), (0, 1))
    que = deque([(start, 0)])  # 큐에 로봇 상태와 경과 시간을 저장
    visited = set([start])  # 방문한 위치와 상태를 저장
    
    # 네 방향 이동 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n and board[x1][y1] == 0 and board[x2][y2] == 0
    
    while que:
        (pos1, pos2), time = que.popleft()
        if pos1 == goal or pos2 == goal:
            return time
        
        x1, y1 = pos1
        x2, y2 = pos2
        
        # 네 방향 이동
        for dx, dy in directions:
            next_pos1 = (x1 + dx, y1 + dy)
            next_pos2 = (x2 + dx, y2 + dy)
            if is_valid(next_pos1, next_pos2) and (next_pos1, next_pos2) not in visited:
                visited.add((next_pos1, next_pos2))
                que.append(((next_pos1, next_pos2), time + 1))
        
        # 회전
        if x1 == x2:  # 가로로 놓여있는 경우
            for i in [-1, 1]:  # 위쪽 또는 아래쪽으로 회전
                if 0 <= x1 + i < n and board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                    # 왼쪽 칸을 축으로 위로 회전
                    if is_valid((x1 + i, y1), (x1, y1)):
                        if ((x1 + i, y1), (x1, y1)) not in visited:
                            visited.add(((x1 + i, y1), (x1, y1)))
                            que.append((((x1 + i, y1), (x1, y1)), time + 1))
                    # 오른쪽 칸을 축으로 위로 회전
                    if is_valid((x2 + i, y2), (x2, y2)):
                        if ((x2 + i, y2), (x2, y2)) not in visited:
                            visited.add(((x2 + i, y2), (x2, y2)))
                            que.append((((x2 + i, y2), (x2, y2)), time + 1))
        elif y1 == y2:  # 세로로 놓여있는 경우
            for i in [-1, 1]:  # 왼쪽 또는 오른쪽으로 회전
                if 0 <= y1 + i < n and board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                    # 위쪽 칸을 축으로 왼쪽으로 회전
                    if is_valid((x1, y1 + i), (x1, y1)):
                        if ((x1, y1 + i), (x1, y1)) not in visited:
                            visited.add(((x1, y1 + i), (x1, y1)))
                            que.append((((x1, y1 + i), (x1, y1)), time + 1))
                    # 아래쪽 칸을 축으로 왼쪽으로 회전
                    if is_valid((x2, y2 + i), (x2, y2)):
                        if ((x2, y2 + i), (x2, y2)) not in visited:
                            visited.add(((x2, y2 + i), (x2, y2)))
                            que.append((((x2, y2 + i), (x2, y2)), time + 1))
    
    return -1

# Example usage:
# board = [
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
#     [0, 0, 0, 0, 0]
# ]
# print(solution(board))  # Expected output: 7
