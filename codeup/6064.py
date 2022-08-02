# a,b,c=map(int, input().split())
# n=(a if (a>=b) else b)
# n2=(b if (b>=c) else c)
# n3=(a if (a>=b) else c)
# print()

# a,b,c=map(int, input().split())
# if(a>=b):
#     if(b>=c):
#         print(c)
# if(a>=b):
#     if(b<=c):
#         print(b)
# if(a<=b):
#     if(a<=c):
#         print(a)
# if(a<=b):
#     if(a>=c):
#         print(c)

a,b,c=map(int, input().split())
print(min(a,b,c))