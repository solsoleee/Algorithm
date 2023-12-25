N=int(input())
a=1
b=N-1
for i in range(1, N+1):
    print(" "*b, end="")
    print("*"*a)
    b-=1
    a+=2