# import sys

# s,p=map(int, sys.stdin.readline().split())
# s_list=sys.stdin.readline()
# a,c,g,t = map(int, sys.stdin.readline().split())

# cnt=0

# for i in range(s-p+1):
#     result=s_list[i:i+p]
#     if result.count('A')>=a and result.count('C')>=c and result.count('G')>=g and result.count('T')>=t:
#         cnt+=1
        
# print(cnt)

import sys
from collections import deque

s,p=map(int, sys.stdin.readline().split())
s_list=sys.stdin.readline()
a,c,g,t = map(int, sys.stdin.readline().split())

dic={'A':0, 'C':0, 'G':0, 'T':0}
left, right = 0, p-1
arr=deque(s_list[left:right])
for i in arr:
    dic[i]+=1

cnt=0

while right < s:
    dic[s_list[right]]+=1
    
    if dic['A'] >=a and dic['C'] >=c and dic['G'] >=g and dic['T'] >=t:
        cnt+=1
    
    dic[s_list[left]]-=1
    left+=1
    right+=1

print(cnt)