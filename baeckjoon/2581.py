M=int(input())
N=int(input())
list=[]
sum=0
for i in range(M,N+1):
    cnt=0
    for j in range(1,N+1):
        if(i%j==0):
            cnt+=1
    if(cnt==2):
        list.append(i)
    elif(cnt==0):
        print(-1)
        exit()

for i in list:
    sum=sum+i
print(sum)
print(min(list))