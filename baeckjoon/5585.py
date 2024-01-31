n=int(input())
n=1000-n
pay_list=[500,100,50,10,5,1]
cnt=0

for pay in pay_list:
    cnt+=n//pay
    n=n%pay
print(cnt)