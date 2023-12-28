alp="abcdefghijklmnopqrstuvwxyz"
alp2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S=input()

for i in S:
    if i.isalpha():
        if i.isupper():
            if alp2.index(i)+13 >= len(alp2):
                print(alp2[alp2.index(i)%13], end="")
            else:
                print(alp2[alp2.index(i)+13], end="")
        else:
            if alp.index(i)+13 >= len(alp):
                print(alp[alp.index(i)%13], end="")
            else:
                print(alp[alp.index(i)+13], end="")
    else:
        print(i, end="")

