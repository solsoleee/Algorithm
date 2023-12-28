T=int(input())
for i in range(T):
    A,B=map(int, input().split())
    for j in range(max(A,B), (A*B)+1):
        if j%A==0 and j%B==0:
            print(j)
            break
