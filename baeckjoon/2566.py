max_list=[]
max_num=0
a,b=0,0
for i in range(9):
    number=list(map(int, input().split()))
    max_list.append(number)
    
for col in range(9):
    for row in range(9):
        if max_num < max_list[col][row]:
            max_num=max_list[col][row]
            a,b=col,row

print(max_num)
print(a+1,b+1, end=" ")