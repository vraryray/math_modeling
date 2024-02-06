import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 500, 0.01)

def bacteria(N, t):
    dmdt = k * N
    return dmdt

N_0 = 1
k = 0.05

N_t = odeint(bacteria, N_0, t)

plt.plot(t, N_t[:,0], label='Размножение бактерий')
plt.title('Размножение бактерий')

plt.savefig('task_1.png')