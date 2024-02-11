# 그래프를 3배로 키워준다
# 90도로 돌리는 함수!!를 만든다
# 새로운 그래프 중앙값에 원래 있는 lock값은 넣는다
# 돌려가면서 다 1이 되는 수를 찾는다 (1를 찾는 함수 만들기!!)
# 만족하지 않으면 다시 옮긴다

def rotation(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result

def check(new_key):
    n = len(new_key) // 3
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if new_key[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 키를 중앙에 넣는다.
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    
    # 돌리는 거 4번 반복 90*4=360이니까
    for r in range(4):
        key = rotation(key)
        # 중앙까지 확인
        for x in range(n * 2):
            for y in range(n * 2):
                # 1씩 돌아가면서 더해줌
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                if check(new_lock) == True:
                    answer = True
                    return answer
                
                # 다시 빼줌
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]        
    return answer