arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(arr)+1)

for i in range(len(arr)):
    count[arr[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
        
        