n,k=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if arr[i][0] == k:
        idx=i

# 동점일 수도 있으니까.. 앞에 같은게 있으면 그걸로 출력
for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break