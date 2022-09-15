from inspect import stack
import sys
N=int(sys.stdin.readline())
stack=[]
for _ in range (N):
    word=sys.stdin.readline().split()
    for i in word:
        print(i[::-1],end=' ')
    