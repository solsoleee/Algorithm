n=int(input())
n_list=list(map(int, input().split()))
n_list.sort()


result=0 #그룹수
cnt=0 #그룹에 포함된 현재 수
for i in n_list:
    cnt+=1
    if cnt >= i:
        result+=1
        cnt=0
        print(i)

print(result)