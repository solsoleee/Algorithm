T=int(input())

for test_case in range(1, T+1):
    arr=input()
    for i in range(1,11):
        if arr[:i]==arr[i:i+i] and arr[i:i+i]==arr[i+i:i+i+i]:
            print(f"#{test_case} {i}")
            break