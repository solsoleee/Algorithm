word=[]
for i in range(5):
    a= input()
    word.append(a)

for col in range(15):
    for row in range(5):
        if col < len (word[row]):
            print(word[row][col], end="")