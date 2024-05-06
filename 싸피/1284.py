T=int(input())

for t in range(1, T+1):
    p,q,r,s,w = map(int, input().split())
    
    a_list=p*w
    if r >= w:
        b_list=q
    else:
        b_list=q+(w-r)*s
    
    print(f'#{t}', end=' ')
    print(min(a_list,b_list))