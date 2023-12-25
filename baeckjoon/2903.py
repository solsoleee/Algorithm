N=int(input())

a=2
total=0

for i in range(1,N+1):
        
    a=a+(a-1)
    total=a*a

print(total)