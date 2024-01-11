import sys
from collections import Counter

N=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

M=int(sys.stdin.readline())
arr_list=list(map(int, sys.stdin.readline().split()))

c=Counter(arr)

for j in arr_list:
    if j in c:
        print(c[j], end=' ')
    else:
        print(0, end=' ' )



# import sys

# d=[0]*500001

# N=int(sys.stdin.readline())
# arr=list(map(int, sys.stdin.readline().split()))

# for i in arr:
#     N[i]+=1
# print(d)