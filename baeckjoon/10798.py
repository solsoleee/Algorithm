word=[]
length=[]
for i in range(5):
    a= input()
    word.append(a)
    length.append(len(word))
print(len(word))

for col in range(5):
    for row in range(len(col)):
        print(word[row][col], end="")