s=list(input())
arr=[]
result=0
for i in s:
    if i.isalpha():
        arr.append(i)
    else:
        i=int(i)
        result+=i
        
arr.sort()
print(*arr,result,sep='')