N,M = map(int, input().split())

A,B=[], []

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    
for j in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for col in range(N):
    for row in range(M):
        print(A[col][row] + B[col][row], end=" ")
    print()