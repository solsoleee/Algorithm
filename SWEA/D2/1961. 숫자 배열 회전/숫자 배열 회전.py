#90도 회전
def change(arr):
    res_arr=[]
    for i in range(N):
        change_arr=[]
        for j in range(N-1, -1, -1):
            change_arr.append(arr[j][i])
        res_arr.append(change_arr)
    return res_arr


T=int(input())

for t in range(1, T+1):
    arr=[]
    N=int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))

    arr_90=change(arr)
    arr_180=change(arr_90)
    arr_270=change(arr_180)
    result=[]
    for i in range(N):
        result.append(
            ''.join(map(str, arr_90[i]))+' '+
            ''.join(map(str, arr_180[i]))+' '+
            ''.join(map(str, arr_270[i]))
        )
    print(f'#{t}')
    for r in result:
        print(r)