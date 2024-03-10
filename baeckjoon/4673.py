arr=[0]*10001


for i in range(1, 9973):
    res=0
    res+=i
    for a in str(i):
        res+=int(a)
    # print(i, res)
    if res <= 10001:
        arr[res]+=1

for j in range(1, len(arr)):
    if arr[j]==0:
        print(j)
    
