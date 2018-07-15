def LCS(X, Y):
    m, n = len(X), len(Y)
    N = [[0] * (n+1) for x in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                N[i][j] = N[i-1][j-1] + 1
            else:
                N[i][j] = max(N[i-1][j], N[i][j-1])
    return N

def retrace(X, Y, N):   #not concise, see 'retrace2' below
    '''reconstruct the common subsequence from matrix N'''
    m, n = len(X), len(Y)
    results = []
    i, j = m, n
    while i > 0 and j > 0:
        left, up, leftup = N[i][j-1], N[i-1][j], N[i-1][j-1]
        if left > up and left > leftup:
            j -= 1
        elif up > left and up > leftup:
            i -= 1
        elif N[i][j] == leftup + 1:
            # print(N[i][j], "->", leftup)
            results.append(X[i-1])
            i -= 1
            j -= 1
        else:
            i -= 1
    return "".join(reversed(results))

def retrace2(X, Y, N):
    m, n = len(X), len(Y)
    results = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            results.append(X[i-1])
            i -= 1
            j -= 1
        elif N[i-1][j] >= N[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(results))

if __name__ == "__main__":
    x = "abcde"
    y = "abcde"
    for each in LCS(x, y):
        print(each)
    N = LCS(x, y)
    if N[len(x) - 1][len(y) - 1] > 0:
        print(retrace2(x, y, LCS(x, y)))