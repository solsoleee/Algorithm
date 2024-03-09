n=int(input())
res=0


for i in range(n):
    arr=[] #저장된거
    front='' #현재거 
    flag=True #확인
    word=input()
    for i in range(len(word)):
        if front!=word[i] and word[i] in arr:
            flag=False
            break
        front=word[i]
        arr.append(word[i])

    if flag==True:
        res+=1

print(res)