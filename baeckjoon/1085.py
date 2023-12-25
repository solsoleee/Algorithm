x,y,w,h=map(int, input().split())
square=[]
square.append(abs(x-w)) 
square.append(abs(y-h))
square.append(x)
square.append(y)

print(min(square))
