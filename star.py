from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(R, vx0, vy0, time):
    t = np.arange(-2*np.pi, 8*np.pi, 0.1)
    x = 12*np.cos(t) + 8*np.cos(1.5*t)**5
    y = 12*np.sin(t) - 8*np.sin(1.5*t)**5

    X = x * np.cos(time) - y * np.sin(time)
    Y = y * np.cos(time) + x * np.sin(time)
    return X, Y


def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='g', label='Ball')

    edge = 40
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Funny turtle')
    
    ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=30)

ani.save('star.gif') 