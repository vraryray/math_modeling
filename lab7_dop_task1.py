from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np 

def circle_move(R):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R*(t - np.sin(t))
    y = R*(1 - np.cos(t))
    return x, y


def animate(i):
    ball.set_data(circle_move(R=2))

if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], color='b', label='Ball')
 
    edge = 15
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
 
    ani = FuncAnimation(fig, animate, frames=180, interval=30)
 
    ani.save('dop_task1.gif') 