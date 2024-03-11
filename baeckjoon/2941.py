
alp=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word=input()
arr=[]
res=0


for a in alp:
    if a in word:
        res+=1
        print(a)

print(res)
print(len(word)-res*2 + res)
        

# if word in a:
#     print(word)

# for i in range(len(word)):
#     arr=word
#     if arr[i: i+1] in a:
#         res+=1
#         word=arr.remove(arr[i: i+1])