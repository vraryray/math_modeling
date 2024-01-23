from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np

def star():
    t = np.arange(,  , 0.1)

    x = 12*np.cos(t) + 8*np.cos(1.5*t)
    y = 12*np.sin(t) - 8*np.sin(1.5*t)

    plt.plot(x, y, lw=3)
    plt.axis('equal')
    plt.savefig('task3.png')

if __name__ == '__main__':
    star()