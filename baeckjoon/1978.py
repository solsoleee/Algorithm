N=int(input())
number=list(map(int, input().split()))
total=0

for i in range(N):
    prime=[]
    for j in range(1, number[i]+1):
        if number[i] % j ==0:
            prime.append(j)
    if len(prime) == 2:
        total += 1

print(total)