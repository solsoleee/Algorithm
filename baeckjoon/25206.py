def grade(x):
    if x=="A+":
        return float(4.5)
    elif x=="A0":
        return float(4.0)
    elif x=="B+":
        return float(3.5)
    elif x=="B0":
        return float(3.0)
    elif x=="C+":
        return float(2.5)
    elif x=="C0":
        return float(2.0)
    elif x=="D+":
        return float(1.5)
    elif x=="D0":
        return float(1.0)
    elif x=="F":
        return float(0.0)

sum =0
total=0
for i in range(20):
    a,b,c=input().split()
    if c=="P":
        pass
    else: 
        total+=float(b)
        sum += float(b) * float(grade(c))

age=sum/total
print(round(age, 6))

