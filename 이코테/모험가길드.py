n = int(input())
arr = list(map(int, input().split()))

arr.sort()  # 공포도 오름차순 정렬
print(arr)
groups = 0  # 만들어진 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in arr:
    count += 1  # 현재 그룹에 모험가 추가
    if count >= i:  # 그룹의 모험가 수가 현재 모험가의 공포도 이상이면
        groups += 1  # 그룹 하나를 만들고
        count = 0  # 다음 그룹을 위해 카운트 초기화

print(groups)
