import sys

alp="abcdefghijklmnopqrstuvwxyz"
result=[0 for _ in range(26)]

S=input()

for i in S:
    result[alp.index(i)]+=1

print(*result)
