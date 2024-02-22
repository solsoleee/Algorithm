def solution(triangle):
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                left = 0  # 이전 행의 왼쪽 대각선 위 값이 없으므로 0으로 설정
            else:
                left = triangle[i-1][j-1]  # 왼쪽 대각선 위의 값

            if j == i:
                up = 0  # 이전 행의 바로 위 값이 없으므로 0으로 설정
            else:
                up = triangle[i-1][j]  # 바로 위의 값

            # 현재 위치를 업데이트 할 때, 왼쪽 대각선 위와 바로 위 중 더 큰 값을 현재 값과 더함
            triangle[i][j] += max(left, up)

    # 마지막 행에서 최대값을 찾아 반환
    answer = max(triangle[n-1])
    return answer
