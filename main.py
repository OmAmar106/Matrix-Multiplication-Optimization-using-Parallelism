import random
import non_optimized_matrix_multiplication as non_opt
import optimized_matrix_multiplication as opt

def func(L):
    for i in L:
        print(*i)

for i in range(20):
    k = 10
    t = random.randint(2,5)
    t1 = random.randint(3,6)
    matA = [[random.randint(1,50) for j in range(k)] for l in range(t)]
    matB = [[random.randint(1,50) for j in range(t1)] for l in range(k)]

    assert non_opt.mul(matA,matB,True)==opt.mul(matA,matB,True)

k = 100
t = random.randint(20,50)
t1 = random.randint(20,50)
matA = [[random.randint(1,50) for j in range(k)] for l in range(t)]
matB = [[random.randint(1,50) for j in range(t1)] for l in range(k)]
print(non_opt.mul(matA,matB,False),opt.mul(matA,matB,False))