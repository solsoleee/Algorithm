a,b=map(int,input().split())
c=int(input())
m=b+c
while(True):
    if(m>=60):
        a=a+1
        if(a>=24):
            a=a-24
        m=m-60
    if(m<60):
        print(a,m,end=' ')            
        break
else:
    print(a,b+c,end=' ')