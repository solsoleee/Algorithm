t=int(input())
for i in range(t):
    h,w,n=map(int, input().split())


    arr = [list(range(1, w+1)) for _ in range(h)]

    y=0#층수
    x=1#번호
    while n>h:
        n-=h
        x+=1

    y+=n
    if arr[y-1][x-1] < 10:
        print(y,0,arr[y-1][x-1],sep='')
    else:
        print(y,arr[y-1][x-1],sep='')