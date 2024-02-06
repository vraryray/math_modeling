import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,  8, 0.1)

def money(N, t):
    dmdt = -k * N * t
    return dmdt

N_0 = 1000
k = 0.08

N_t = odeint(money, N_0, t)

plt.plot(t, N_t[:,0])
plt.title('Денежные инвестиции')

plt.savefig('task_2.png')