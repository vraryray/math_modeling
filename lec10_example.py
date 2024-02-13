import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

x = np.arange(0, 50, 0.01)

def diff_func(z, x):
    y, omega = z

    dtheta_dt = omega
    domega_dt = np.sin(y)*omega - 3*x*y - 5

    return dtheta_dt, domega_dt

y0 = 0.01
omega0 = 0.05
z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1], 'b', color = 'pink',  label = 'theta(x)')
plt.legend()
plt.savefig('example.png')