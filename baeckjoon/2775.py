t=int(input())

# for i in range(t):
#     k=int(input())
#     n=int(input())
#     cnt=0
#     for j in range(k-1, k):
#         for l in range(1, n+1):
#             cnt+=l
#     print(cnt)
    
def fibo(k, n):
    cnt=0
    if k==0:
        for i in range(n):
            cnt+=i
        return cnt
    else:
        return fibo(k-1, n)

k=int(input())
n=int(input())

print(fibo(k,n))