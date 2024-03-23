def row(x, n):  # 가로 검사
    for i in range(9):
        if n == sudoku[x][i]:  # 이미 같은 숫자가 행에 있으면 False
            return False
    return True

def column(y, n):  # 세로 검사
    for i in range(9):
        if n == sudoku[i][y]:  # 이미 같은 숫자가 열에 있으면 False
            return False
    return True

def square(x, y, n):  # 3x3 칸 검사
    x_start = (x // 3) * 3
    y_start = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if n == sudoku[x_start + i][y_start + j]:  # 칸 내에 이미 같은 숫자가 있으면 False
                return False
    return True

def find(n):
    if n == len(blank):  # 모든 빈 칸을 채웠다면 스도쿠 출력 후 종료
        for r in sudoku:
            print(*r)
        exit()

    x, y = blank[n]  # 빈 칸의 위치
    for i in range(1, 10):  # 1부터 9까지 숫자를 시도
        if column(y, i) and row(x, i) and square(x, y, i):  # 세로, 가로, 3x3 칸 모두 유효하면 숫자를 채움
            sudoku[x][y] = i
            find(n + 1)  # 다음 빈 칸으로
            sudoku[x][y] = 0  # 백트래킹, 실패했다면 원래대로 돌림

import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

find(0)
