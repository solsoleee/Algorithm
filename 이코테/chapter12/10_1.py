def rotate(lock): # 90도 방향으로 돌리는 함수
    n = len(lock) # 열의 수 
    m = len(lock[0]) # 행의 수
    result = [[0]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = lock[i][j]
    return result


def check(new_lock): #다 1인지 확인하는 함수
    length=len(new_lock)//3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if new_lock[i][j]!=1:
                return False
    return True


def solution(key, lock):
    #lock을 3배로 만들어줌
    #3배로 만들어준거 중앙에 lock을 넣어줌
    #key를 돌리면서 방향 확인하면서 반복 넣어줌
    answer=False
    n=len(key)
    m=len(lock)
    new_lock=[[0]*(m*3) for _ in range(m*3)]
    #중앙에 lock을 넣어줌
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m]+=lock[i][j]
    
    #4가지 방향에 대해서 확인
    # 4가지 방향에 대해서 확인
    for _ in range(4):  # 변수 이름 변경
        key = rotate(key)  # 함수 이름 변경
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠를 끼워넣기
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j]-=key[i][j]
    answer=False
    return answer