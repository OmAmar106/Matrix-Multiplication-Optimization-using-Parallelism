import random
import non_optimized_matrix_multiplication as non_opt
import optimized_matrix_multiplication as opt
import strassen
from collections import defaultdict
import matplotlib.pyplot as plt
import os

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

diffarr = defaultdict(list)

for k in range(6,100):
    L3 = []
    L4 = []
    matA = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    matB = [[random.randint(1,50) for j in range(k)] for l in range(k)]
    diff = [2,3,4,5,6,int(k**0.25),int(k**0.5)]
    for j in range(len(diff)):
        if j==len(diff)-1:
            diffarr["N^0.5"].append(opt.mul(matA,matB,False,diff[j]))
        elif j==len(diff)-2:
            diffarr["N^0.25"].append(opt.mul(matA,matB,False,diff[j]))
        else:
            diffarr[diff[j]].append(opt.mul(matA,matB,False,diff[j]))
    L.append(non_opt.mul(matA,matB,False))

for j in diffarr:
    L5 = diffarr[j]
    # plt.plot(L, marker='o', label='Brute')
    try:
        s = str(j*j)
    except:
        s = j+'^2'
    plt.plot(L5, marker='o', label=s+' Thread')
    plt.legend()
    plt.xlabel('Matrix Size')
    plt.ylabel('Time (seconds)')
    plt.title('Matrix Multiplication Time Comparison')
    plt.grid(True)
    plt.show()
