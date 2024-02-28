n=int(input())

for i in range(n):
    cnt=0
    res=0
    arr=input()
    for j in arr:
        if j == 'O':
            cnt+=1
        if j =='X':
            cnt=0
        res+=cnt

    print(res)