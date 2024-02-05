
stack=[input()]
arr=[]
cnt=0

for i in stack:
    if i == '(' or i == '[':
        arr.append(i)
    elif i == ')':
        arr.pop()
        arr.append(int(2))
    elif i ==']':
        if (arr.pop()).isdigit():
            cnt*=3
        arr.append(int(3))