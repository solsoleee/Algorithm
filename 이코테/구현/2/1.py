# q=list(input())

# result=0

# d1=[2,1] # x축, y축, 순서
# d2=[-2,1]
# d3=[2,-1]
# d4=[-2,-1]

# ord(q[0])+2
# q[1]+=1

# q[1]+=2
# ord(q[0])+1
# print(ord('a'))

# for i in range(8):
#     for j in range(2):
#         ord(q[0])+d1[i]
#         q[1]

command=list(input())

result=0

steps=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]

row=int(ord(command[0])-ord('a'))+1
column=int(command[1])

for step in steps:
    new_row=row+step[0]
    new_column=column+step[1]
    
    if new_row<=8 and new_column<=8 and new_row>=1 and new_column>=1:
        print(new_row, new_column)      
        result+=1

print (result)