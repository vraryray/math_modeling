import numpy as np

N = 4
M = 2
A = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        if i > 0 and j < 0:
            A[i, j] = np.sin((N * (i + 1)) + (M * (j + 1)))
        else:
            A[i, j] = np.sin((N * i) + (M * j))

for i in range(N):
        for j in range(M):               
            if A[i, j] < 0:
                A[i, j] = 0

print(A)                