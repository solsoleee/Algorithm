N=int(input())

square=[[0 for _ in range(101)] for _ in range(101)]

print(square)

for i in range(N):
    x,y=list(map(int, input().split()))
    
    for row in range(x,x+10):
        for col in range(y,y+10):
            square[row][col]=1