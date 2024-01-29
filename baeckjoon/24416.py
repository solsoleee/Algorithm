n=int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1;  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2));

f=[0] * 41
f[1]=1
f[2]=1
global cnt

def fibonacci(n) :
    cnt=0
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2];  # 코드2
        cnt+=1
    return cnt;

print(fib(n))
print(fibonacci(n))