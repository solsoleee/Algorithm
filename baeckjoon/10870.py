n=int(input())
def s(n):
    if n==0 or n==1:
        return n
    else:
        return s(n-1)+s(n-2)
print(s(n))