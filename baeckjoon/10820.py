import sys
while(True):
    
    num=[0 for _ in range(4)]
    S=sys.stdin.readline().rstrip('\n')
    if not S:
        break
    for i in S:
        if i.isdecimal():
            num[2]+=1
        elif i.isalpha():
            if i.isupper():
                num[1]+=1
            else:
                num[0]+=1
        else:
            num[3]+=1
    print(*num)
