from collections import Counter
import sys
n=int(input())
arr=[]
for i in range(n):
    num=int(sys.stdin.readline())
    arr.append(num)

arr.sort(reverse=True)
print(int(round(sum(arr)/n, 0)))
print(arr[(n//2)])

arr.sort()
cnt = Counter(arr).most_common(2)

if len(cnt)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
print(max(arr)-min(arr))