def LCSlength(X, Y):
    m=len(X)
    n=len(Y)
    L=[[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j], L[i][j-1])
    return L

def printLcs(L, X, Y):
    i, j = len(X), len(Y)
    result = []

    while i > 0 and j > 0:
        if L[i][j] == L[i-1][j]:
            i -= 1
        elif L[i][j] == L[i][j-1]:
            j -= 1
        else:
            result.append(X[i-1])
            i -= 1
            j -= 1
    
    return ''.join(reversed(result))

def main():
    
    X = input("A 입력: ").split()
    Y = input("B 입력: ").split()

    # LCS 알고리즘을 적용
    L = LCSlength(X, Y)
    # 결과를 출력
    lcs = printLcs(L, X, Y)
    print("LCS:", lcs)

if __name__ == "__main__":
    main()