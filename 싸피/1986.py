T=int(input())

for t in range(1, T+1):
    res=0
    N=int(input())
    for i in range(1, N+1):
        if i%2!=0:
            res=res+i
        else:
            res=res-i
    print(f'#{t} {res}')