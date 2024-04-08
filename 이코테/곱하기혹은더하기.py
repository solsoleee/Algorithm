num=input()
res=int(num[0])
for i in range(1, len(num)):
    if (res == 0 or res ==1) or (int(num[i])==0 or int(num[i])==1):
        res+=int(num[i])
        print(res)
    else:
        res*=int(num[i])

print(res)