T=int(input())

for t in range(1, T+1):
    a,b,c,d = map(int, input().split())
    hour=a+c
    
    min=b+d
    if min >= 60:
        hour+=1
        min = min % 60
        
    if hour > 12:
        if hour % 12 == 0:
            hour = 12
        else:
            hour = hour % 12
    
    print(f'#{t} {hour} {min}')