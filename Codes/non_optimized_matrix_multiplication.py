import time

def mul(mat,mat1,flag):
    start = time.time()
    ans = [[0]*(len(mat1[0])) for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat1[0])):
            ans[i][j] = sum([mat[i][k]*mat1[k][j] for k in range(len(mat1))])
    if flag:
        return ans
    else:
        return time.time()-start