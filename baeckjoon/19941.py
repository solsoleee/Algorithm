n,k=map(int, input().split())

s=input()
# cnt=0
 
# for i in range(n-1,-1,-1):
#     if s[i]=='P':
#         for j in range(1,k+1):
#             if (i-k>=0) and (s[i-k]=='H'):
#                 cnt+=1
#                 print(i-k)

# print(cnt)

s=s.replace('HP', '1')
s=s.replace('PH', '1')

s=list(s)
for i in s:
    if i == '1':
        s.remove(i)
print(s)