n=list(map(int, input()))

length=len(n)//2
result=0
for i in range(length):
    result+=n[i]

if sum(n[length:]) == result:
    print("LUCKY")
else:
    print("READY")
