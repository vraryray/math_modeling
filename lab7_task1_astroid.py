from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np

def astroid(R=5):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R * (np.cos(t)**3)
    y = R * (np.sin(t)**3)

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('task1_2.png')

if __name__ == '__main__':
    astroid()