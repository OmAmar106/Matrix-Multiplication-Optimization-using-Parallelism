import random
import non_optimized_matrix_multiplication as non_opt
import optimized_matrix_multiplication as opt
for i in range(20):
    k = 4
    matA = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    matB = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    assert(non_opt.mul(matA,matB,True)==opt.mul(matA,matB,True))
print("")