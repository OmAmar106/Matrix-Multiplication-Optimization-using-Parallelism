import time

def mul(mat,mat1,flag):
    start = time.time()
    ans = [[0]*(len(mat1[0])) for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat1[0])):
            sumi = 0
            for k in range(len(mat1)):
                sumi += mat[i][k]*mat1[k][j]
            ans[i][j] = sumi
    if flag:
        return ans
    else:
        return time.time()-start