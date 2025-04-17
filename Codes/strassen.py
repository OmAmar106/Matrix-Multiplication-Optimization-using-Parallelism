import time
import math

def next_power_of_two(n):
    return 1 << (n - 1).bit_length()

def pad_matrix(M, size):
    padded = [[0] * size for _ in range(size)]
    for i in range(len(M)):
        for j in range(len(M[0])):
            padded[i][j] = M[i][j]
    return padded

def unpad_matrix(M, rows, cols):
    return [row[:cols] for row in M[:rows]]

def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen_core(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    M1 = strassen_core(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_core(add_matrix(A21, A22), B11)
    M3 = strassen_core(A11, sub_matrix(B12, B22))
    M4 = strassen_core(A22, sub_matrix(B21, B11))
    M5 = strassen_core(add_matrix(A11, A12), B22)
    M6 = strassen_core(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_core(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix

def mul(mat, mat1, flag):
    start = time.time()
    a_rows, a_cols = len(mat), len(mat[0])
    b_rows, b_cols = len(mat1), len(mat1[0])

    size = next_power_of_two(max(a_rows, a_cols, b_rows, b_cols))
    padded_A = pad_matrix(mat, size)
    padded_B = pad_matrix(mat1, size)

    padded_C = strassen_core(padded_A, padded_B)
    result = unpad_matrix(padded_C, a_rows, b_cols)

    if flag:
        return result
    else:
        return time.time() - start
