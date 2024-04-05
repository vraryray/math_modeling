import numpy as np
import time
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation, ArtistAnimation 

fig = plt.figure(figsize=(10, 6))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.arange(-2*np.pi, 2*np.pi, 0.1)
xgrid, ygrid = np.meshgrid(x, y)

phasa = np.arange(0, 2*np.pi, 0.1)
frames = []

for p in phasa:
    zgrid = np.sin(xgrid+p) * np.sin(ygrid)/(xgrid*ygrid)

    line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='pink')
    frames.append([line])

ani = ArtistAnimation(
    fig,
    frames,
    interval = 30,
    blit = True,
    repeat=True
)

plt.show()