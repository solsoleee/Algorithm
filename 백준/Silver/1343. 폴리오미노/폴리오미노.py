s=input()

dic={"XXXX":"AAAA", "XX":"BB"}

for a,b in dic.items():
    s=s.replace(a,b)


if "X" in s:
    print("-1")
else:
    print(s)

