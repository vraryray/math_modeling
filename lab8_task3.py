import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def flying(v, t):
    dmdt = g - k * v**2
    return dmdt

N_0 = 1
k = 0.2
g = 9.8
v_0 = 0

N_t = odeint(flying, v_0, t)

plt.plot(t, N_t[:,0])
plt.title('Free falling')

plt.savefig('task_3.png')