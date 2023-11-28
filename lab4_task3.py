import numpy as np
from constant import gravity_accelaration as g

def energy(m, h, v):
    E = (m*v**2/2) + m*g*h 
    return E
print(energy(m = 10, h = 5, v = 2))