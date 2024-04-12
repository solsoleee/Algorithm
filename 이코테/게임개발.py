N=input()

mid=len(N)//2

a=N[:mid]
b=N[mid:]

sum_a=0
sum_b=0
for i in a:
    sum_a+=int(i)
for j in b:
    sum_b+=int(j)

if sum_a==sum_b:
    print("LUCKY")
else:
    print("READY")
    