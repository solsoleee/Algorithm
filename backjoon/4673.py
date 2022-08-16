def d(n):
    number=n
    num=list(str(n))
    for i in range(len(num)):
        number+=int(num[i])
    return number
a=list(range(1,10001))
for n in range(1,10001):
    if d(n) in a:
        a.remove(d(n))
for i in range(len(a)):
    print(a[i])