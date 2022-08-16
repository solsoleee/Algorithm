A,B,V=map(int,input().split())
x=(V-B)/(A-B)
v=A*x-B*x+B
if(V==v):
    x+=1
    print(int(x))
else:
    print(int(x))

    
