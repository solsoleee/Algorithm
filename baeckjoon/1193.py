X=int(input())

line=1

while X > line:
    X-=line
    line+=1

print(X)
print(line)

if line % 2==0:
        for i in range(1, X+1):
            if i > 1 and line > 1:
                line-=1
            else:
                pass
        print(X,"/",line,sep="")
else:
    for i in range(1, X+1):
        if i > 1 and line > 1:
            line-=1
        else:
            pass
    print(line,"/",X,sep="")
    