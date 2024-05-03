T=int(input())

for t in range(1, T+1):
    res=list(map(int, input().split()))
    res.remove(max(res))
    res.remove(min(res))
    print(f'#{t} {round((sum(res)/len(res)))}')