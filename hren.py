from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

guitarLad = np.array([
    [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],            
    [329.63, 349.23, 369.99, 391.99, 415.30, 440.00, 466.00, 494.00, 523.00, 554.00, 587.00],  
    [246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 391.99, 415.30, 440.00],  
    [196.00, 207.65, 220.00, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23],  
    [146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94, 261.63],  
    [110.00, 116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00], 
    [82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47, 130.81, 138.59, 146.83]])    



def animate(i):
    x = np.arange(0, 8*np.pi, 0.01)
    y = 2* np.sin(x* np.pi/i) + 5.5*np.cos(x/i) + np.cos(x*i)
    ball.set_data(x, y)


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')

edge = 10
plt.axis('equal')
ax.set_xlim(0, 25)
ax.set_ylim(-5, 5)
    
ani = FuncAnimation(fig, animate, frames=np.arange(0.1, 10, 0.01), interval=30)

ani.save('hrennn.gif')