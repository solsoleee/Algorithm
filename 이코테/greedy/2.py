n,m,k=map(int, input().split())

arr=list(map(int, input().split()))

# result=0
# a=arr.pop(arr.index(max(arr)))
# while m>0:
#     arr.append(a)
#     for i in range(k):
#         result+=max(arr)
#         m-=1
#         if m<=0:
#             break
#     if m<=0:
#         break
#     a=arr.pop(arr.index(max(arr)))
#     result+=max(arr)
#     m-=1

# print(result)

arr.sort()

first=arr[-1]
two=arr[-2]

print(first, two)