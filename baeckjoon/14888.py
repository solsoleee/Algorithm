from itertools import permutations

n=int(input())

arr=list(map(int, input().split()))
command=list(map(int, input().split()))
commands=['+', '-', '*', '%']
ans=[]
i=0
for c in command:
    if c!=0:
        for _ in range(c) :
            ans.append(commands[i])
    i+=1

res_sum=[]

for a in list(permutations(ans, len(ans))):
    ans_sum=arr[0]
    for i in range(0, len(ans)):
        if a[i]=='+':
            ans_sum+=arr[i+1]
        elif a[i]=='*':
            ans_sum*=arr[i+1]
        elif a[i]=='-':
            ans_sum-=arr[i+1]
        else:
            if ans_sum<0:
                ans_sum=(-ans_sum)//arr[i+1]
                ans_sum=(-ans_sum)
            else:
                ans_sum//=arr[i+1]
    res_sum.append(ans_sum)
print(max(res_sum))
print(min(res_sum))
