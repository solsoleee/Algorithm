f=int(input())

arr=[]
for i in range(f):
    arr.append(int(input()))
    
total=0
total += arr[0]+arr[len(arr)-1]

for j in range(1,len(arr)-3):
    print(max(arr[j], arr[j+1]))
    print("aa",arr[j])
    total += max(arr[j], arr[j+1])
print(total)