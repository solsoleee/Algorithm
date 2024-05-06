T=int(input())

for t in range(1, T+1):
    s=input()
    mid=len(s)//2

    res1=s[:mid]

    res2=s[mid+1:]
    print(f'#{t}', end=' ')
    if res1[::-1]==res2:
        if res1==res1[::-1] and res2==res2[::-1]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")