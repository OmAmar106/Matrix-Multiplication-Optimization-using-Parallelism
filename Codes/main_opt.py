from optimized_matrix_multiplication import mul
import random
import matplotlib.pyplot as plt

k = 200

matA = [[random.randint(1,1000) for i in range(k)] for j in range(k)]
matB = [[random.randint(1,1000) for i in range(k)] for j in range(k)]

L = []

for i in range(1,k+1):
    L.append(mul(matA,matB,False,i))


plt.plot([i for i in range(1,k+1)],L)
plt.show()