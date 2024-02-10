# 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다
# 현재 부분합이 M과 같다면 카운트한다
# 현재 부분합이 M보다 작으면 end를 1 증가시킨다
# 현재 부분합이 M보다 크거나 작으면 start를 1 증가시킨다
# 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다

#특정 합 찾기
# n=5
# m=5
# data=[1,2,3,2,5]

# count=0
# interval_sum=0
# end=0

# for start in range(n):
#     #end를 가능한 만큼 이동시키기
#     while interval_sum <= m and end<n:
#         interval_sum+=data[end]
#         end+=1
#     if interval_sum==m:
#         count+=1
#     interval_sum+=data[start]

#합집합

n,m=3,4
a=[1,3,5]
b=[2,4,6,8]

result=[0]*(n+m)
i=0
j=0
k=0

#모든 원소가 결과 리스트에 담길 때까지 반복
while i<n or j<m:
    #리스트 B의 모든 원소가 처리되었거나, 리스트A의 원소가 더 적을 때
    if j>m or (i<n and a[i]<=b[j]):
        result[k]=b[j]
        