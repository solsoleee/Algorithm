s=list(input())
cnt=0
for i in range(len(s)):
    if s[i] in 'ABC':
        cnt+=3
    if s[i] in 'DEF':
        cnt+=4
    if s[i] in 'GHI':
        cnt+=5
    if s[i] in 'JKL':
        cnt+=6
    if s[i] in 'MNO':
        cnt+=7
    if s[i] in 'PQRS':
        cnt+=8
    if s[i] in 'TUV':
        cnt+=9
    if s[i] in 'WXYZ':
        cnt+=10
print(cnt)