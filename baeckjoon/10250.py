n=int(input())
x=1
y=1
for i in range(n):
    a,b,c=map(int,input().split())
    if(c-a<=0):
        y=c
        print(y,x)
    while(c-a>0):
        x+=1
        y=c-a
        if(c-a<=0):
            y=c
        break
    print(y,x)
            
        