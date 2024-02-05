n=int(input())
arr=list(map(int, input().split()))
arr.sort(reverse=True)
if n%2==1:
    result=arr.pop(0)
else:
    result=0
for i in range(0, n//2):
    result=max(result, arr[i]+arr[-i-1])

print(result)