word=input()
list=["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt=0
for i in list:
        word=word.replace(i,'*')
print(len(word))