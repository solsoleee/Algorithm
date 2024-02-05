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

#두개를 더하는 이유는 제일 최소값을 만들기 위해서 그걸 넘으면 안되니까
#부족했던 이유는 홀수, 짝수 구분을 안해준거