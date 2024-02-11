#S가 같은 줄에 있는지 없는지 세어주는 함수
#완전탐색으로 O의 3개의 위치를 정함
#dfs로 구현해야지

#나의 문제점 S를 찾는것을 함수로 표현 못하겠다 ㅜㅜ

#선생님 위치 저장해놓는거 기억해놓으니 편하다
#for x,y in res 이거! 튜플로 바로 꺼내기 편하다

from itertools import combinations

n=int(input())
graph=[] 
res=[] #선생님 위치
spaces=[] #모든 빈 공간 위치 정보

for i in range(n):
    graph.append(list(input().split()))

    for j in range(n):
        if graph[i][j]=='T':
            res.append((i,j))
        if graph[i][j]=='X':
            spaces.append((i,j))

#같은 줄에 s가 있나보기 발견: True, 미발견: False
def watch(x,y,direction):
    #왼쪽 방향으로 감시
    if direction==0:
        while y>=0 :
            if graph[x][y]=='O': #발견X
                break
            if graph[x][y]=='S':
                return True
            y-=1
    #오른쪽 방향으로 감시
    if direction==1:
        while y<n :
            if graph[x][y]=='O': #발견X
                break
            if graph[x][y]=='S':
                return True
            y+=1
    #위쪽 방향으로 감시
    if direction==2:
        while x>=0 :
            if graph[x][y]=='O': #발견X
                break
            if graph[x][y]=='S':
                return True
            x-=1
    #아래쪽 방향으로 감시
    if direction==3:
        while x<n:
            if graph[x][y]=='O': #발견X
                break
            if graph[x][y]=='S':
                return True
            x+=1
    return False

#장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    for x,y in res:
        #4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x,y,i): #감지되면
                return True
    return False

find=False # 힉생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부 (최종정답)

for data in combinations(spaces,3):
    for x,y in data:
        graph[x][y]='O'
    if not process():
        find=True
        break
    for x,y in data:
        graph[x][y]='X'

if find:
    print('YES')
else:
    print('NO') 
