import numpy as np

h = 100
a = np.pi / 3
b = 30
from lab3_1 import gravity_acceleration as g

up = g * h * np.tan(b)**2
down = 2 * np.cos(a) * (1 - np.tan(b) * np.tan(a))
v = np.sqrt(up / down)

print(v)