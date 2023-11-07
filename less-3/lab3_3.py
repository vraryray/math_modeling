import numpy as np

Xo  = 0
Vox = 1
Yo = 0
Voy = 0
t = np.arange(0, 5, 0.1)
from lab3_1 import gravity_acceleration as g

x = Xo + (Vox * t)
y = Yo + Voy * t -(g * t**2 / 2)

coords = np.zeros((len(t), 3))
for i in range(len(t)):
    coords[i, 0] = t[i]
    coords[i, 1] = x[i]
    coords[i, 2] = y[i]
print(coords)       