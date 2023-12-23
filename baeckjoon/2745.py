word="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a,b=input().split()
sum=0

a=a[::-1]

for i,n in enumerate(a):
    sum+=(int(b)**i)*(word.index(n))

print(sum)