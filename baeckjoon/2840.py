n,k = map(int, input().split())

arr = [0]*(n+1)
pointer=0
check=True

for i in range(k):
    num, s = input().split()
    num = int(num)
    print((pointer+num)%n)
    if arr[(pointer+num)%n]!=0:
        if arr[(pointer+num)%n]==s:
            pointer=(pointer+num)%n
            pass
        else:
            print("!")
            check=False
            break
    else:
        arr[(pointer+num)%n] = s
        pointer=(pointer+num)%n
    
if check:
    print(arr[0:n])
    for i in range(pointer,num,-1):
        print(i)
        print(arr[i])
