import matplotlib.pyplot as plt 
import numpy as np 

def wow_hyperbola(Xmin = -10, Xmax = 10, N = 100):
    x = np.arange(0.01, 10, 0.01)
    y = 1/x

    plt.plot(x, y, color = 'm', label = 'hyperbola', marker = 'o', ms = 5)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('My hyperbola')

    plt.savefig('fig_task2.png')

if __name__ == '__main__':
    wow_hyperbola()

def wow_hyperbola1(Xmin = -10, Xmax = 10, N = 100):
    x = np.arange(-10, -0.01, 0.01)
    y = 1/x

    plt.plot(x, y, color = 'm', label = 'hyperbola', marker = 'o', ms = 5)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('My hyperbola')

    plt.savefig('fig_task2.png')

if __name__ == '__main__':
    wow_hyperbola1() 