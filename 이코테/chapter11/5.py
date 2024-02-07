# 중복을 없앤다음에 count를 해서 자기 자신을 제외한 나머지 수를 count 한다
# count 할 때는 나보다는 큰 수다
# 차례대로 카운트, 볼링공의 무게 arr에서

n,m=map(int, input().split())

k=list(map(int, input().split()))
# k.sort()
# cnt=0

# for i in k:
#     for j in range(n):
#         if k[j]> i:
#             cnt+=1

# print(cnt)

arr=[0]*11

for i in k:
    arr[i]+=1

result=0

for j in range(1, m+1):
    n-=arr[i] #j가 1일때 n은 1을 제외하고 4가된다
    result+=arr[i]*n #1의 개수와 선택지를 곱한다