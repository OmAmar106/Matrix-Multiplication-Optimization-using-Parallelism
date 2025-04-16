import random
import non_optimized_matrix_multiplication as non_opt
import optimized_matrix_multiplication as opt
import strassen

def func(L):
    for i in L:
        print(*i)

for i in range(20):
    k = 10
    t = k
    t1 = k
    matA = [[random.randint(1,50) for j in range(k)] for l in range(t)]
    matB = [[random.randint(1,50) for j in range(t1)] for l in range(k)]
    assert non_opt.mul(matA,matB,True)==opt.mul(matA,matB,True)

print("No Inconsistency in the values of the matrix.")

L = []
L1 = []
L2 = []
L5 = []
L6 = []
L7 = []

for k in range(4,100):
    L3 = []
    L4 = []
    matA = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    matB = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    diff = [1,2,int(k**0.25),-1]
    for j in range(4):    
        L4.append(opt.mul(matA,matB,False,diff[j]))
    L.append(non_opt.mul(matA,matB,False))
    L2.append(L4[0])
    L5.append(L4[1])
    L6.append(L4[2])
    L7.append(L4[3])

import matplotlib.pyplot as plt
plt.plot(L, marker='o', label='Brute')
plt.plot(L2, marker='o', label='1 Thread')
plt.plot(L5, marker='o', label='2 Thread')
plt.plot(L6, marker='o', label='N^(1/4) Thread')
plt.plot(L7, marker='o', label='N^(1/2) Thread')

plt.legend()
plt.xlabel('Matrix Size')
plt.ylabel('Time (seconds)')
plt.title('Multiplication Time Comparison')
plt.grid(True)
plt.show()