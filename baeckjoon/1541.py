n=input().split('-')

arr=[]
for i in range(len(n)):
    arr.append(n[i].split('+'))
print(arr)

for j in range(len(arr)):
    if len(arr[j]) > 1:
        print(arr[j])
        
        
