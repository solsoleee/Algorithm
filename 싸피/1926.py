N=int(input())
arr=['3','6','9']

for i in range(1, N+1):
    count=0
    num=str(i)
    for j in range(len(num)):
        if num[j] in arr:
            count+=1
    if count > 0 :
        num='-'*count
    print(num, end=' ')