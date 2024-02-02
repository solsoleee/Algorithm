# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    

# print(fibo(int(input())))

n=int(input())

d=[0]*46

d[1]=1
d[2]=1
for i in range(3, n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])