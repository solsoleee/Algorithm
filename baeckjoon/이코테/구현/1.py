n=int(input())
command=input().split()

arr=[ [i] * n for i in range(n)]

print(arr)

one=1 #행
two=1 #열

for c in command:
    if c=='R' and two<n:
        two+=1
    elif c=='L' and two>1:
        two-=1
    elif c=='U' and one>1:
        one-=1
    elif c=='D' and one<n:
        one+=1

print(one, two)