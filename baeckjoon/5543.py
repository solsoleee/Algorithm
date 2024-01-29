arr=[]
arr_list=[]
for i in range(3):
    arr.append(int(input()))
for j in range(2):
    arr_list.append(int(input()))
    
print(min(arr)+min(arr_list)-50)