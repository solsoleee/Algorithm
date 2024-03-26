

def row(n,x): #x축 검사, x줄에 n이 있다면 체크
    for i in range(9):
        if n==sudocu[x][i]:
            return False
    return True

def column(n,y): #y축 검사, y줄에 n이 있다면 체크
    for i in range(9):
        if n==sudocu[i][y]:
            return False
    return True

def check(n,x,y): #x,y에 n이 있나 체크
    x_start=(x//3) *3
    y_start=(y//3) *3
    for i in range(3):
        for j in range(3):
            if n==sudocu[x_start+i][y_start+j]:
                return False
    return True

def find(n):
    if n==len(blank):
        for s in sudocu:
            print(*s)
        exit()
    x,y = blank[n]
    for i in range(1,10):
        if row(i,x) and column(i,y) and check(i,x,y):
            sudocu[x][y]=i
            find(n+1)
            sudocu[x][y]=0

sudocu=[list(map(int, input().split())) for _ in range(9)]

blank=[]
for i in range(9):
    for j in range(9):
        if sudocu[i][j]==0:
            blank.append((i,j)) #x,y임         
find(0)