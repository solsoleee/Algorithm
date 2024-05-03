T=int(input())

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    res=[]
    N=int(input())
    for c in change:
        if N >= c: 
            res.append(N//c)
            N=N%c
        else:
            res.append(0)

    print(f'#{t}')
    print(*res)