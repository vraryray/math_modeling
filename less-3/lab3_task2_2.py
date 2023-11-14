import numpy as np

T = 200
E = 300
from lab3_1 import boltzmann_constant as k
from lab3_1 import planck_constant as h
from lab3_1 import euler_number as e

first = 2 / np.sqrt(np.pi)
second = h / ((k * T)**(3/2))
third = e**(-(E)/(k * T))
forth = E**(T / 2)

N = first * second * third * forth
print(N)