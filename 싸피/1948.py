T=int(input())

for t in range(1, T+1):
    a,b,c,d = map(int, input().split())
    res=0
    if a==c:
        res=d-b+1
    else:
        res=0
        for i in range(a+1, c):
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
                res+=31
            elif i==2:
                res+=28
            else:
                res+=30
        
        if a==2:
            res+=(28-b+1)
        elif a==4 or a==6 or a==9 or a==11:
            res+=(30-b+1)
        else:
            res+=(31-b+1)
        
        res+=d
    
    print(f'#{t} {res}')