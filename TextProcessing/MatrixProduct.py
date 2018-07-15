def matrix_pro(d):
    n = len(d) - 1
    N = [[0 for x in range(n)] for y in range(n)]
    for dis in range(1, n): #the length(+1) of subproblems
        for i in range(0, n - dis):
            j = i + dis
            N[i][j] = min([N[i][k] + N[k][j] + d[i]*d[k + 1]*d[j + 1] for k in range(i, j)])
    return N

if __name__ == "__main__":
    d = [100, 5, 10, 2, 5]
    for each in matrix_pro(d):
        print(each)
    print(matrix_pro(d)[0][3])