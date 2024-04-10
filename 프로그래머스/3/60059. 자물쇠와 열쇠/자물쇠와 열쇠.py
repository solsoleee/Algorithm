def solution(key, lock):
    
    
    #2차원 배열 회전
    def rotation(a):
        n=len(key)
        m=len(key[0])
        rotation_key=[[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotation_key[j][n-i-1] = a[i][j]
        return rotation_key
    
    #3배로 확장
    def new_big_lock():
        n=len(lock)
        new_lock=[[0]*(3*n) for j in range(3*n)]
        for i in range(n, n*2):
            for j in range(n, n*2):
                new_lock[i][j]=lock[i-n][j-n]
        return new_lock
    
    #가운데 부분 1이 맞는지 체크 모두 1이면 됨
    def check(new_lock):
        for i in range(n, n*2):
            for j in range(n, n*2):
                if new_lock[i][j]!=1:
                    return False
        return True
                
    new_big_lock=new_big_lock() #3배로 확장
    m=len(key)
    n=len(lock)
    for r in range(4): #회전 4번할 때 동안 만족하는지
        key=rotation(key) #열쇠회전
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_big_lock[x+i][y+j]+=key[i][j]
                
                if check(new_big_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_big_lock[x+i][y+j]-=key[i][j]
    return False