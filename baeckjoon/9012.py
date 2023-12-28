N=int(input())
for i in range(N):
    a=input()
    b=[]
    for j in a:
        if j=="(":
            b.append(j)
        elif j==")":
            if b:
                b.pop()
            else:
                print("NO")
                break
        else:
            if b:
                print("NO")
            else:
                print("YES")