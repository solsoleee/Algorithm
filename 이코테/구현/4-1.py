n=int(input())

command=list(input().split())

x,y=0,0
def direction(command):
    global x,y
    if command=='R':
        if x+1<n:
            x+=1
            return x
    elif command=='L':
        if x-1>=0:
            x-=1
            return x
    elif command=='U':
        if y-1>=0:
            y-=1
            return y
    else:
        if y+1<n:
            y+=1
            return y
            
for i in command:
    direction(i)
print(y+1, x+1)
