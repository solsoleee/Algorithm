N,M,K = map(int, input().split())

arr=list(map(int, input().split()))

arr.sort()

data1=arr[N-1]
data2=arr[N-2]

result=0

while True:
    for i in range(K):
        if M==0:
            break    
        result+=data1
        M=M-1
    if M==0:
        break
    result+=data2
    M=M-1

print(result)