n=int(input())
arr=[]


for i in range(n):
    name, a, b, c = input().split()
    arr.append([name, int(a), int(b), int(c)])
    
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])


