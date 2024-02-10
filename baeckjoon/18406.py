n=list(map(int,input()))

length=len(n)//2

a=n[:length]
b=n[length:]

if sum(a)==sum(b):
    print("LUCKY")
else:
    print("READY")