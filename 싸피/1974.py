

#정사각형 확인
def square(arr):
    check=[]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(3):
                for v in range(3):
                    if arr[i+k][j+v] in check:
                        return False
                    check.append(arr[i+k][j+v])
            check=[]
    return True


#가로 확인
def check_row(arr):
    for i in range(9):
        for j in range(1, 10):
            if arr[i].count(j) > 1:
                return False
    return True

#세로 확인
def check_column(arr):
    check=[]
    for i in range(9):
        for j in range(9):
            if arr[j][i] in check:
                return False
            check.append(arr[j][i])
        check=[]
    return True

T=int(input())

for t in range(1, T+1):
    arr=[]
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    if check_column(arr) and check_row(arr) and square(arr):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')