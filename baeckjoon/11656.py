S=input()
word=[]

for i in range(len(S)):
    word.append(S[i:])

word.sort()

for i in word:
    print(i)