T=int(input())

for t in range(1, T+1):
    N=int(input())
    
    i=1
    arr=[]
    while True:
        res=N*i
        arr.extend(map(int, str(res)))
        arr=list(set(arr))
        if len(arr)==10:
            break
        i+=1
    print(f'#{t}', end=' ')
    print(res)

    