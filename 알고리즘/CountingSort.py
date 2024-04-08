arr=[4,7,9,1,2,5,2,3,4]

count = [0] * (max(arr) + 1)

for num in arr:
    count[num] +=1 

# 각 요소가 정렬된 배열에서 정확히 어디에 위치해야 하는지를 알 수 있다
for i in range(1, len(count)):
    count[i] += count[i-1]
    
result = [0] * len(arr)

for num in arr:
    idx = count[num]
    result[idx-1]=num
    count[num]-=1
    
    