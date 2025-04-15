def mul(mat,mat1):
    ans = [[0]*(len(mat1[0])) for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sumi = 0
            for k in range(len(mat[0])):
                sumi += mat[i][k]*mat1[k][j]
            ans[i][j] = sumi
    return 1
