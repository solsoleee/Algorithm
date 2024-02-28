from itertools import combinations

first = True  # 첫 번째 테스트 케이스인지 확인하기 위한 플래그

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    
    if not first:  # 첫 번째 테스트 케이스가 아니라면 줄바꿈을 추가
        print()
    first = False  # 첫 번째 테스트 케이스가 아니므로 플래그를 False로 설정
    
    arr = arr[1:]
    res = []
    for x in combinations(arr, 6):
        res.append(list(x))
    
    res.sort()
    
    for i in res:
        print(*i)
