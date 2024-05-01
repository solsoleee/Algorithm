t=int(input())

for _ in range(t):
    arr=list(map(int, input().split()))
    print(round(sum(arr)/len(arr)))