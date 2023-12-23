chess=[1,1,2,2,2,8]
number=list(map(int,input().split()))
list=[0,0,0,0,0,0]
for i in range(6):
    chess[i]=int(chess[i])
    list[i]=chess[i]-number[i]
for i in list:
    print(i,end=" ")