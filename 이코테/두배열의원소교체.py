n,k=map(int, input().split())

a_list=list(map(int, input().split()))

b_list=list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)
cnt=0
for i in range(n):
    if cnt==k:
        break
    if b_list[i] > a_list[i]:
        a_list[i], b_list[i] = b_list[i], a_list[i]
        cnt+=1
        
print(sum(a_list))