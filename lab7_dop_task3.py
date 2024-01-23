from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np

def star():
    t = np.arange(-2*np.pi, 8*np.pi, 0.1)

    x = 12*np.cos(t) + 8*np.cos(1.5*t)
    y = 12*np.sin(t) - 8*np.sin(1.5*t)

    plt.plot(x, y, color = 'b', ms = 5)

    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Star')
    plt.grid()

    plt.axis('equal')
    plt.savefig('task3.png')

if __name__ == '__main__':
    star()