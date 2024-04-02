import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

guitarLad = np.array([
    [20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000, 20000],             #пауза
    [329.63, 349.23, 369.99, 391.99, 415.30, 440.00, 466.00, 494.00, 523.00, 554.00, 587.00],  #1струна
    [246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 391.99, 415.30, 440.00],  #2струна
    [196.00, 207.65, 220.00, 233.08, 246.94, 261.63, 277.18, 293.66, 311.13, 329.63, 349.23],  #3струна
    [146.83, 155.56, 164.81, 174.61, 185.00, 196.00, 207.65, 220.00, 233.08, 246.94, 261.63],  #4струна
    [110.00, 116.54, 123.47, 130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 185.00, 196.00],  #5струна
    [82.41, 87.31, 92.50, 98.00, 103.83, 110.00, 116.54, 123.47, 130.81, 138.59, 146.83]])     #6струна

mas = np.loadtxt('example.txt', delimiter=' ', dtype=np.float64)




fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(0, 7))
line, = ax.plot([], [], lw=3)
line1, = ax.plot([], [], lw=3)
line2, = ax.plot([], [], lw=3)
line3, = ax.plot([], [], lw=3)
line4, = ax.plot([], [], lw=3)
line5, = ax.plot([], [], lw=3)
def init():
    line.set_data([], [])
    return line,
for key in  mas:
        freg = (guitarLad[int(key[0])][int(key[1])])
def animate(i):
    freg = (guitarLad[int(mas[i][0])][int(mas[i][1])])
    if mas[i][0]== 1:
        pass
        
    
    x = np.linspace(0, 4, 1000)
    y1 = np.sin(x)/4
    y2 = np.sin(x)/4
    y3 = np.sin(x)/4
    y4 = np.sin( x)/4
    y5 = np.sin(x )/4
    y6 = np.sin(x)/4
    line.set_data(x, y1+1)
    line1.set_data(x, y2+2)
    line2.set_data(x, y3+3)
    line3.set_data(x, y4+4)
    line4.set_data(x, y5+5)
    line5.set_data(x, y6+6)
    return line,line1,line2,line3,line4,line5,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=(len(mas)), interval=200, blit=True)

anim.save('rtata.gif')