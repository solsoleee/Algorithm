N=int(input())

cnt=0
while N>0:
    if N%5==0:
        cnt=cnt+N//5
        break
        N=N%5
    
    N-=3
    cnt+=1

print(cnt)