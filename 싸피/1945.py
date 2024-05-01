
t=int(input())
for _ in range(t):
    a,b,c,d,e=0,0,0,0,0
    N=int(input())
    while N!=1:
        if N%11==0:
            e+=1
            N=N//11
        elif N%7==0:
            d+=1
            N=N//7
        elif N%5==0:
            c+=1
            N=N//5
        elif N%3==0:
            b+=1
            N=N//3
        else:
            N=N//2
            a+=1
        if N==1:
            break

    print(a,b,c,d,e)
    
    
    
    