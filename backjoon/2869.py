A,B,V=map(int,input().split())
x=(V-B)/(A-B)

if((V-B)%(A-B)==0):
    print(int(x))
else:
    x+=1
    print(int(x))

    
